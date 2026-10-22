# Chapter 11 practice program: deleteLargeFiles.py
# This program finds files larger than 100MB by default and deletes them.

import os
import send2trash

from pathlib import Path

def delete_large_files(path: str|Path, file_size=104857600):
    for folder_name, subfolders, filenames in os.walk(Path(path)):
        for filename in filenames:
            file = Path(folder_name) / filename
            if os.path.getsize(file) > file_size:
                send2trash.send2trash(file)
                print(f'Deleted {file}')

    print(f'All files larger than {str(int(file_size/1024/1024))} MB in {path} were deleted.')

delete_large_files(Path.home() / 'Downloads')