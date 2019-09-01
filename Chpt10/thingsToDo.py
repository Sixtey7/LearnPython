#Thing 1
print('---Thing 1---')
from datetime import date, datetime
import time
now = date.today()
thing1Out = open('today.txt', 'wt')
thing1Out.write(now.isoformat())
thing1Out.close()

#Thing 2
print('---Thing 2---')
thing2In = open('today.txt', 'rt')
today_string = thing2In.read()
print("Today String %s" % today_string)

#Thing 3
print('---Thing 3---')
fmt = "%Y-%m-%d"
new_time_struct = time.strptime(today_string, fmt)
new_date = date(new_time_struct.tm_year, new_time_struct.tm_mon, new_time_struct.tm_mday)
print("New Date Parsed From File:", new_date)

#Thing 4
print('---Thing 4---')
import os
filesInDir = os.listdir('.')
print ("Files in Directory:", filesInDir)

#Thing 5
print('---Thing 5---')
filesInParent = os.listdir('..')
print ("Files in Parent Directory:", filesInParent)

#Thing 6
print('---Thing 6---')
# 10.6 Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between one and five, print the current time, and then exit.
import multiprocessing
from random import randrange
def do_a_thing():
    timeToWait = randrange(1, 6)
    time.sleep(timeToWait)
    print("Slept %s seconds and now it is:" % timeToWait, datetime.today())

for n in range(3):
    p = multiprocessing.Process(target=do_a_thing)
    p.start()

#Thing 7
print('---Thing 7---')
birthDate = date(1986, 12, 4)
print("I was born:", birthDate)

#Thing 8
print('---Thing 8---')
print('I was born on a:', birthDate.strftime('%A'))

#Thing 9
print('---Thing 9---')
from datetime import timedelta
oneThousandDaysOld = birthDate + timedelta(10000)
print('I was 10,000 days old on:' , oneThousandDaysOld)