# Chapter 11 practice program: convertFilesDateFormat
# Change all files in a directory that has an american date format to european date format.
# Assume the months and days always use two digits, and that files with non-date matches don’t exist.

import os
import random
import re
import shutil

from datetime import datetime
from pathlib import Path

def convert_dates(path: str|Path) -> None:
    folder = Path(path)
    print(f'Preparing to convert all files with American date format to European date format in {folder}.')

    for folder_name, subfolders, filenames in os.walk(folder):
        cwd = Path(folder_name)

        for filename in filenames:
            pattern = r'\d{2}-\d{2}-\d{4}'
            match = re.search(pattern, filename)
            eu_date = str(datetime.strptime(match.group(), '%m-%d-%Y').strftime('%d-%m-%Y'))
            converted_filename = re.compile(pattern).sub(eu_date, filename)
            #shutil.move(cwd / filename, cwd / converted_filename)
            print(f'Renamed {cwd / filename} to {cwd / converted_filename}')

    print(f'All filles with American dates in their names were converted to European dates.')

def create_dir_and_files(path: str|Path) -> None:
    folder = Path(path)
    os.chdir(folder)

    for i in range(3):
            os.mkdir(f'spam{i}')

    for folder_name, subfolders, filenames in os.walk(folder):
        for i in range(5):
            month = str(random.randint(1, 12)).zfill(2)
            day = str(random.randint(1, 31)).zfill(2)
            year = str(random.randint(2000, 2026))
            with open(f'{folder_name}/spam{month}-{day}-{year}.txt', 'w') as file:
               pass

            print(f'Created file {folder_name}/spam{month}-{day}-{year}.txt')

convert_dates(Path.home() / 'spamfiles')
#create_dir_and_files(Path.home() / 'spamfiles')