import os
import random
from datetime import datetime


def init_main_dir(main_dir="user_name"):
    try:
        os.mkdir(main_dir)
        print(f"Folder '{main_dir}' created successfully at {datetime.now}.")
        return 1
    except FileExistsError:
        print(f"Folder '{main_dir}' exists already.\n")
        return 1
    except OSError as e:
        print(f"Error occurred while creating folder '{main_dir}'.\n")
        return 0

def init_sub_dir(sub_dir, main_dir="user_name"):
    

def combine(sections, main_folder, output, flag, keywords):
    for folder in sections:
        folder_path = os.path.join(main_folder, folder)
        options = os.listdir(folder_path)
        i = random.randint(1, len(options))
        file_path = os.path.join(folder_path, str(i)+".txt")
        try:
            append(output, read(file_path, flag, keywords))
        except FileNotFoundError:
            print(f"Error: '{file_path}' not found")


def read(filename, flag, keywords):
    with open(filename, 'r') as file:
        file_contents = key_words(file.read(), flag, keywords)
        print(file_contents, "\n")  # Uncomment this line to get a print of what's happening
        return file_contents


def key_words(content, flag, keywords):
    edited_content = []
    for word in content.split():

        if word[0] == flag:
            if word[1:] in list(keywords.keys()):
                word = keywords[word[1:]]
            elif word[1:-1] in list(keywords.keys()):  # this one is for potential punctuation (1 symbol)
                word = keywords[word[1:-1]] + word[-1]
            elif word[1:-2] in list(keywords.keys()):  # this one is for potential punctuation (2 symbols)
                word = keywords[word[1:-2]] + word[-2:]
        edited_content.append(word)
    return ' '.join(edited_content)


def append(filename, new_contents):
    with open(filename, 'a') as file:
        file.write(new_contents)
        file.write("\n\n")


def clear(filename):
    with open(filename, 'w'):
        pass
