# PyClock

A clock util for raspberry pi.

### Installation

`sudo apt install arp-scan`

`pip3 install termcolor pyfiglet`

Place your script somewhere, like under `/home/pi/py-clock`

Add a crontab with `crontab -e`: mind the default output being `tty1`

`* * * * * python3 clock/clock.py > /dev/tty1 2>&1`

Add the local network scanner to your `sudo crontab -e` as network scanning requires `sudo`

For name resolution edit `arp_list.py` as for some reason
I could not get that to work dynamically.

Enjoy!

### Other, better software

It does not support fyglets though.

https://github.com/wtfutil/wtf


MIT