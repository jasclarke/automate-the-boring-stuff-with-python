# Chapter 19 Practice program: friday13finder.py
# This program finds the next 10 Friday 13th dates

import datetime

today = datetime.datetime.now()
next_day = datetime.timedelta(days=1)
num_fridays = 0

print('The next 10 Friday the 13th are in the following months:\n')

while num_fridays < 10:
    if today.weekday() == 4 and today.day == 13:
        print(f'{today.strftime('%B,').ljust(10)} {today.strftime('%Y')}')
        num_fridays += 1

    today += next_day

print('\n\nThe previous 10 Friday the 13th were in the following months:\n')

today = datetime.datetime.now()

while num_fridays > 0:
    if today.weekday() == 4 and today.day == 13:
        print(f'{today.strftime('%B,').ljust(10)} {today.strftime('%Y')}')
        num_fridays -= 1

    today -= next_day