# https://autbor.com/simplecountdown.py - A simple countdown script

import subprocess
import time

time_left = 60

while time_left > 0:
    print(time_left)
    time.sleep(1)
    time_left = time_left - 1

# At the end of the countdown, play a sound file.
#subprocess.run(['start', 'alarm.wav'], shell=True) # Windows
subprocess.run(['open', 'chapter19/alarm.wav']) # MacOS and Linux