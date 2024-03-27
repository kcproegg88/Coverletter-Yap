import os
import random
from datetime import datetime


class DataBase:
    def __init__(self, main_dir, sub_dirs):
        self.main_dir = str(main_dir)
        self.sub_dirs = sub_dirs
        self.output_file = None
        self.flag = None
        self.keywords = None

    def init_setup(self):
        num_paragraphs = len(self.sub_dirs)
        working = self.init_main_dir()

        paragraphs = 0
        while working:
            working = self.create_sub_dir(self.sub_dirs[paragraphs])
            for i in range(3):
                self.create_file(f"{i + 1}.txt", self.sub_dirs[paragraphs], True)
            paragraphs += 1
            if paragraphs >= num_paragraphs:
                print(f"Setup Successful, {num_paragraphs} paragraphs initialized.\n")
                break

    def init_main_dir(self):
        try:
            os.mkdir(self.main_dir)
            print(f"Main Folder '{self.main_dir}' created successfully at {datetime.now()}.")
            return 1
        except FileExistsError:
            print(f"Main Folder '{self.main_dir}' exists already.")
            return 1
        except OSError as e:
            print(f"Error occurred while creating folder '{self.main_dir}': {e}\n")
            return 0

    def create_sub_dir(self, sub_dir):
        nested_folder_path = os.path.join(self.main_dir, sub_dir)
        try:
            os.mkdir(nested_folder_path)
            print(f"\n\tFolder '{sub_dir}' created successfully under '{self.main_dir}' at {datetime.now()}.")
            return 1
        except FileExistsError:
            print(f"\n\tFolder '{sub_dir}' exists under '{self.main_dir}' already.")
            return 1
        except OSError as e:
            print(f"Error occurred while creating folder '{sub_dir}' under '{self.main_dir}': {e}\n")
            return 0

    def create_file(self, file_name, sub_dir="", sample=False):
        nested_folder_path = os.path.join(self.main_dir, sub_dir)
        file_path = os.path.join(nested_folder_path, file_name)
        try:
            if os.path.exists(file_path):
                print(f"\t\tText file '{file_name}' already exists inside '{nested_folder_path}'.")
                return 1
            with open(file_path, 'w') as file:
                if sample:
                    file_written_name = file_name[:-4]
                    sub_dir_written_name = " ".join(sub_dir.split("_"))
                    file.write(f"This is the sample {sub_dir_written_name}, version {file_written_name}: My name is "
                               f"[name], I want to work at [company] as a [position]. You can contact me at [email].")
                    print(f"\t\tText File '{file_name}' created successfully under '{nested_folder_path}'.")
                return 1
        except OSError as e:
            print(f"Error occurred while creating file '{file_name}' under '{nested_folder_path}': {e}\n")
            return 0

    def normalize_setup(self):
        for sub_dir in self.sub_dirs:
            self.normalize_sub_dir(sub_dir)

    def normalize_sub_dir(self, sub_dir):
        nested_folder_path = os.path.join(self.main_dir, sub_dir)
        files = os.listdir(nested_folder_path)

        sorted_files = [""] * len(files)
        unsorted_files = []
        for i in range(len(files)):
            try:
                sorted_files[int(files[i][:-4]) - 1] = files[i]
            except (ValueError, IndexError):
                unsorted_files.append(files[i])
                print(f"File '{files[i]}' is out of order inside '{sub_dir}'.")
            except Exception as e:
                print(f"\nError processing file name '{files[i]}' inside '{sub_dir}': {e}\n")

        for i in range(len(sorted_files)):
            if sorted_files[i] == "":
                try:
                    new_name = os.path.join(nested_folder_path, f"{i + 1}.txt")
                    old_name = os.path.join(nested_folder_path, unsorted_files.pop(-1))
                    os.rename(old_name, new_name)
                except OSError as e:
                    print(f"\nError processing file unsorted file inside '{sub_dir}: {e}\n")

        if len(unsorted_files) == 0:
            print(f"Files inside of '{sub_dir}' have successfully been organized.")
        else:
            print(f"\nThere has been some error somewhere in '{sub_dir}'.\n")

    def display_dir(self, show_all=False):
        print(f"The main directory is {self.main_dir} and consists of:")
        print(f"\t{self.sub_dirs}")
        if show_all:
            for sub_dir in self.sub_dirs:
                print(f"Sub Directory {sub_dir} consists of:")
                nested_folder_path = os.path.join(self.main_dir, sub_dir)
                files = os.listdir(nested_folder_path)
                print(f"\t{files}")

    def combine(self, output_file, flag, keywords):
        self.create_file(output_file)
        self.clear()
        self.output_file = output_file
        self.flag = flag
        self.keywords = keywords

        for sub_dir in self.sub_dirs:
            nested_folder_path = os.path.join(self.main_dir, sub_dir)
            files = os.listdir(nested_folder_path)
            selection = random.randint(1, len(files))
            file_path = os.path.join(nested_folder_path, f"{selection}.txt")
            self.append(self.read(file_path))
            print(f"{sub_dir} added.")

    def clear(self):
        with open(self.output_file, 'w') as file:
            pass

    def append(self, content):
        file_path = os.path.join(self.main_dir, self.output_file)
        with open(file_path, 'a') as file:
            file.write(content)
            file.write("\n\n")

    def read(self, file_path):
        with open(file_path, 'r') as file:
            file_contents = file.read()

        edited_content = []
        for word in file_contents.split():

            if word[0] == self.flag:
                if word[1:] in list(self.keywords.keys()):
                    word = self.keywords[word[1:]]
                elif word[1:-1] in list(self.keywords.keys()):  # this one is for potential punctuation (1 symbol)
                    word = self.keywords[word[1:-1]] + word[-1]
                elif word[1:-2] in list(self.keywords.keys()):  # this one is for potential punctuation (2 symbols)
                    word = self.keywords[word[1:-2]] + word[-2:]
            edited_content.append(word)
        return ' '.join(edited_content)