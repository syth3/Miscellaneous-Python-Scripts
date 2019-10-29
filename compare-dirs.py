import os
import sys
import shutil
from pathlib import Path

source_dir = ""
dest_dir = ""

# Add --relative and -r flags to print a relative path
# Add an option for the relative and absolute paths to be printed to a csv file. Maybe one sheet for each secton printed?

if len(sys.argv) == 1:
    source_dir = input("Input source dir: ")
    dest_dir = input("Input dest dir: ")
# Path("C:/Users/CSEC GA/Documents/Test/source_dir")
if len(sys.argv) == 2:
    source_dir = sys.argv[1]
    dest_dir = input("Input dest dir: ")
if len(sys.argv) == 3:
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]
#Path("C:/Users/CSEC GA/Documents/Test/dest_dir")
source_dir = Path(source_dir)
dest_dir = Path(dest_dir)

source_dir_files = set()
for curr_dir, dirs, files in os.walk(source_dir):
    for file in files:
        full_path = Path(curr_dir) / file
        source_dir_files.add(full_path.relative_to(source_dir))

dest_dir_files = set()
for curr_dir, dirs, files in os.walk(dest_dir):
    for file in files:
        full_path = Path(curr_dir) / file
        dest_dir_files.add(full_path.relative_to(dest_dir))

diff = dest_dir_files - source_dir_files
num_dashes = 20
#print("="*num_dashes + str(len(diff)) + " File(s) in \"" + dest_dir.name + "\" that are not in \"" + source_dir.name + "\"" + "="*num_dashes)
print("File Name (" + str(len(diff)) + " total)" + "\t" + "Full Path")
for file in diff:
    full_dir = dest_dir / file
    if not full_dir.parts[2] == "Virtual Machines" and file.name[0] != '~' and file.name[0] != '.' and file.name != "desktop.ini":
        print(file.name + "\t", end="")
        #print(file)
        print(dest_dir / file)

diff = source_dir_files - dest_dir_files
#print("="*num_dashes + str(len(diff)) + " File(s) in \"" + source_dir.name + "\" that are not in \"" + dest_dir.name + "\"" + "="*num_dashes)
for file in diff:
    print(file.name + "\t", end="")
    #print(file)
    print(source_dir / file)
