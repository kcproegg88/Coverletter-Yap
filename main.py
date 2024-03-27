import cldb

main_dir = "your_name"
#  add all paragraph folders to this folder

output_file = "cover_letter.txt"

num_paragraphs = 3
#  edit num_paragraphs depending on number of paragraphs in between intro and conclusion

flag = "["
#  edit the flag which calls for the replacement

keywords = {"name]": "Ben Simmons",
            "phone]": "1-800-525-0102",
            "email]": "NPIC@state.gov",
            "company]": "US Department of Defense",
            "position]": "F-22 Raptor Pilot"}


def main():
    sub_dirs = ["introduction"]
    [sub_dirs.append("paragraph_"+str(i+1)) for i in range(num_paragraphs)]
    sub_dirs.append("conclusion")

    cover_letter = cldb.DataBase(main_dir, sub_dirs)
    cover_letter.init_setup()
    cover_letter.combine(output_file, flag, keywords)


if __name__ == "__main__":
    main()
