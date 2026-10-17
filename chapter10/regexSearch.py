# Chapter 10 Practice Program: regexSearch.py
# Find a text from all .txt files in a folder.

import re

from pathlib import Path

files_paths = Path('./chapter10').glob('*.txt')
regex = re.compile(input('Enter regular expression or search term:\n'))
results = list()

for file_path in files_paths:
    with open(file_path, 'r', encoding='UTF-8') as file:
        file_content = file.read()

    matches = regex.findall(file_content)
    num_matches = len(matches)

    if num_matches > 0:
        results.append(f'Path: {file_path}\nCount: {num_matches}\nContent: {file_content}\n\n')

if len(results) > 0:
    for index, result in enumerate(results): 
        if index == 0: print('SEARCH RESULTS:\n')
        print(result)
else:
    print('No matches found.')