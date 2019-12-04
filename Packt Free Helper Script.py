import sys
import os
import shutil
from pathlib import Path

def main ():
    if len(sys.argv) != 2:
        print("Forgot Book Name")
        exit(1)
    book_name = sys.argv[1]
    packt_book_path = Path("C:/Users/Jake/OneDrive - rit.edu/Documents/Tech Books/Free/Packt Free")
    new_book_path = packt_book_path / book_name
    if new_book_path.exists():
        print("Book path already exisits in Tech Books folder")
        exit(1)
    else:
        os.mkdir(new_book_path)
    
    # Move books from "Downloads/Pack Downloads" folder to the folder inside of "Tech Books"
    packt_downloads_path = Path("C:/Users/Jake/OneDrive - rit.edu/Downloads/Packt Downloads")
    if not packt_downloads_path.exists():
        os.mkdir(packt_downloads_path)
    for curr_dir, dirs, files in os.walk(packt_downloads_path):
        for file in files:
            shutil.move(packt_downloads_path / file, new_book_path / file)
    
    # Rename Files
    for curr_dir, dirs, files in os.walk(new_book_path):
        for file in files:
            file_name_extension = os.path.splitext(file)[1]
            if file_name_extension == "zip":
                os.rename(new_book_path / file, str(new_book_path / book_name) + " Code Files" + file_name_extension)
            else:
                os.rename(new_book_path / file, str(new_book_path / book_name) + file_name_extension)
main()