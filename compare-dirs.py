import os
import sys
import shutil
from pathlib import Path

source_dir = ""
dest_dir = ""

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
num_dashes = 30
print("="*num_dashes + str(len(diff)) + " File(s) in dest_dir that are not in source_dir" + "="*num_dashes)
for file in diff:
    print(file)

diff = source_dir_files - dest_dir_files
print("="*num_dashes + str(len(diff)) + " File(s) in source_dir that are not in dest_dir" + "="*num_dashes)
for file in diff:
    print(file)
