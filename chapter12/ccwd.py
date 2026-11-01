# Chapter 12 program: ccwd.py (provided in the chapter)
# Copy current working directory or relative supplied path.

import pyperclip
import os
import sys

if len(sys.argv) > 1:
    os.chdir(sys.argv[1])

pyperclip.copy(os.getcwd())