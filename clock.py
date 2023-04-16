# Import a new font style:
# pyfiglet -L clock/dohmono.flf
# change terminal cursor to invisible: (into .bashrc)
# echo -e "\e[?1c"
# run
# clear > /dev/tty1 2>&1 && python3 clock/clock.py > /dev/tty1 2>&1
# crontab it too for every minute!
# * * * * * python3 clock/clock.py > /dev/tty1 2>&1


from termcolor import cprint
from pyfiglet import figlet_format
import os, sys
from datetime import datetime
from terminal import move, clear
from weather import weather
from arp_list import printUsers
from pytz import timezone

message_file_name = 'message.txt'

now = datetime.now()

current_time_h = now.strftime("   %H")
current_time_m = now.strftime("       %M")
current_time = now.strftime("%H %M")
current_date = now.strftime("%B     %d      %a                   ")

screen_height = size = os.get_terminal_size().lines
screen_width = size = os.get_terminal_size().columns

## CLOCK
move(5, 0)
cprint(figlet_format(current_time, font='dohmonosq', justify="center", width=screen_width), 'green', attrs=['concealed'])


## MESSAGE
move(25, 0)
if (os.path.exists(os.path.join(sys.path[0], message_file_name))):
    with open(os.path.join(sys.path[0], message_file_name)) as f:
        lines = f.readlines()
        cprint(figlet_format(lines[0], font='bannerf', width=screen_width, justify="center"), 'blue')


## Date today
move(61, 0)
cprint(figlet_format(current_date, font='doom', width=screen_width, justify="right"),
       'white')


## Global Clock - print pacific time
move(0, 0)

western = timezone('US/Pacific')
format = '%H:%M'
print('Pacific: ', datetime.now(western).strftime(format))


## WEATHER
move(47, 0)
try:
    print(weather.get_weather())
except:
    print('no weather data :(')


## Network
# printUsers() - this needs super user.
# if I run this script in super user, pyfiglet does not find the local flf files.

move(0, 0)