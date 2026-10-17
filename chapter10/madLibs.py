# Chapter 10 Practice Program: MadLibs.py
# Reads in text files and lets the user add their own text anywhere
# the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

import re

with open('chapter10/madLibs.txt', 'r', encoding='UTF-8') as file:
    content = file.read()

print(content)

pattern = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
matches = pattern.findall(content)

for match in matches: 
    user_word = input(f'Enter an {match.lower()}:\n')
    content = re.compile(match).sub(user_word, content, count=1)

print(content)
with open('chapter10/happyLibs.txt', 'w', encoding='UTF-8') as file:
    file.write(content)