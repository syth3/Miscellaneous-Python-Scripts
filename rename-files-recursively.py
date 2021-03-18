import os
import sys
from pathlib import Path


WINDOWS_DISALLOWED_FILENAME_CHARACTERS = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']


class Input:
    def __init__(self, target_dir, remove_text, replace_text):
        """
        Init method for Input class
        :param target_dir: Directory to start searching in
        :param remove_text: Text to remove from filenames
        :param replace_text: Text to replace the removed text from filenames
        """
        self.target_dir = Path(target_dir)

        remove_text_split = []
        for character in remove_text:
            remove_text_split.append(character)
        self.remove_text = remove_text_split

        self.replace_text = replace_text


def gather_input():
    if len(sys.argv) < 4:
        target_dir = input("Input target_dir: ")
        remove_text = input("Input characters to remove from filenames "
                            "(input will be parsed into individual characters): ")
        replace_text = input("Input text to insert into filenames: ")
    else:
        target_dir = sys.argv[1]
        remove_text = sys.argv[2]
        replace_text = sys.argv[3]
    if remove_text.lower() == "windows":
        remove_text = WINDOWS_DISALLOWED_FILENAME_CHARACTERS
    return Input(target_dir, remove_text, replace_text)


def debug(user_input):
    print("target_dir:", user_input.target_dir)
    print("remove_text:", user_input.remove_text)
    print("replace_text:", user_input.replace_text)


def rename_files(user_input):
    for subdir, dirs, files in os.walk(user_input.target_dir):
        print("subdir:", subdir)
        print("dirs:", dirs)
        print("files:", files)
        print()


def main():
    user_input = gather_input()
    # debug(user_input)
    rename_files(user_input)


if __name__ == '__main__':
    main()
