# Chapter 11 practice program: renumberFiles.py
# This program closes the numbering gap for files with a specified prefix in a single folder.
# Added challenge: A function that creates gaps

import re
import shutil

from pathlib import Path

def renumber_files(path: str, prefix: str, min_digits: int) -> None:
    folder = Path(path)
    files = list(folder.glob(prefix + '*'))
    files.sort()

    print('Retrieved all files with the prefix: ' + prefix)
    print(f'Checking for numbering gaps in {folder}')

    for index, file in enumerate(files):
        file_stem = file.stem
        file_num = int(re.search(r'\d+$', file_stem).group())
        file_count = index + 1

        if file_num != (file_count):
            destination = folder / (prefix + str(file_count).zfill(min_digits) + ''.join(file.suffixes))
            shutil.move(file, destination)
            print(f'Renamed {file} to {destination}')

    print(f'All numbering gaps have been removed from {path} for files with a prefix of {prefix}')

def renumber_files_with_gap(path: str, prefix: str, min_digits: int, gap_num: int) -> None:
    folder = Path(path)
    files = list(folder.glob(prefix + '*'))
    files.sort()
    num_files = len(files)

    for num in range(num_files, gap_num - 1, -1):
        index = num - 1
        destination = folder / (prefix + str(num + 1).zfill(min_digits) + ''.join(files[index].suffixes))
        shutil.move(files[index], destination)
        print(f'Renamed {files[index]} to {destination}')

#renumber_files(Path.home() / 'spamfiles', 'spam', 3)
renumber_files_with_gap(Path.home() / 'spamfiles', 'spam', 3, 42)