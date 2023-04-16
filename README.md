# PyClock

A clock util for raspberry pi.

I had a screen and a raspberry lying around and I did not have a clock.
Here is one. With wttr.in weather forecast.

### Installation

`sudo apt install arp-scan`

`pip3 install termcolor pyfiglet pytz`

Place your script somewhere, like under `/home/pi/py-clock`

Add a crontab with `crontab -e`: mind the default output being `tty1`

`* * * * * python3 clock/clock.py > /dev/tty1 2>&1`

Add the local network scanner to your `sudo crontab -e` as network scanning requires `sudo`

For name resolution edit `arp_list.py` as for some reason
I could not get that to work dynamically.

Create a `location.txt` under weather if you want it to work.

Check it with wttr.in with curl:

`curl 'wttr.in/:help'`

Enjoy!

### Other, better software

It does not support fyglets though.

https://github.com/wtfutil/wtf


MIT