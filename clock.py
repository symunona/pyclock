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
from terminal import move
import socket

message_file_name = 'message.txt'

def show_network_status ():
    move(55, 0)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        print(s.getsockname()[0] + ' <- pi')
        s.close()
    except:
        print("no network")

show_network_status()

now = datetime.now()

current_time_h = now.strftime("   %H")
current_time_m = now.strftime("       %M")
current_time = now.strftime("%H %M")
current_date = now.strftime("%B  %d   %a")

screen_height = size = os.get_terminal_size().lines
screen_width = size = os.get_terminal_size().columns


move(10, 0)

cprint(figlet_format(current_time, font='dohmonosq', justify="center", width=screen_width), 'green', attrs=['concealed'])
#cprint(figlet_format(current_time_h, font='dohmonosq'), 'green', attrs=['concealed'])
#cprint(figlet_format(current_time_m, font='dohmonosq'), 'green')


if (os.path.exists(os.path.join(sys.path[0], message_file_name))):
    with open(os.path.join(sys.path[0], message_file_name)) as f:
        lines = f.readlines()
        move(40, 0)
        # print(lines[0])
        cprint(figlet_format(lines[0], font='bannerf', width=screen_width, justify="center"), 'blue')


move(60, 0)

cprint(figlet_format(current_date, font='doom', width=screen_width, justify="center"),
       'white')


move(0, 0)

#print(screen_width, screen_height)
