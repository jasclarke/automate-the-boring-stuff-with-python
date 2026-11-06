# A simple stopwatch program.

import time
import pyperclip

# Display the program's instructions.
print('Press Enter to begin and to mark laps. Ctrl-C quits.')
input() # Press Enter to begin.
print('Started.')
start_time = time.time() # Get the first lap's start time.
last_time = start_time
lap_number = 1

# Start tracking the lap times.
lap_results = []

try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        lap_output = f'Lap #{str(lap_number).rjust(2)}: {str(total_time).rjust(5)} ({str(lap_time).rjust(5)})'
        print(lap_output, end='')
        lap_results.append(lap_output)
        lap_number += 1
        last_time = time.time() # Reset the last lap time.
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
    pyperclip.copy('\n'.join(lap_results))
    print('Lap results copied to the clipboard.')