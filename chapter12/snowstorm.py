# Chapter 12 practice program: snowstorm.py
# Text-based snowstorm animation.

import os
import random
import time
import sys

TOP     = chr(9600)
BOTTOM  = chr(9604)
FULL    = chr(9608)

# Set the snowstorm density to the command line argument:
DENSITY = 4

if len(sys.argv) > 1:
    DENSITY = int(sys.argv[1])

def clear():
    os.system('clear' if os.name == 'posix' else 'nt')

while True:
    clear() # Clear the terminal window.

    # Loop over each row and column:
    for y in range(20):
        for x in range(40):
            if random.randint(0, 99) < DENSITY:
                # Print snow:
                print(random.choice([TOP, BOTTOM]), end='')
            else:
                # Print empty space:
                print(' ', end='')
        print() # Print a newline.

    # Print the snow-covered ground:
    print(FULL * 40 + '\n' + FULL * 40)
    print('(Ctrl-C to stop.)')

    time.sleep(0.2) # Pause for a bit.