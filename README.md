# PyClock

A clock util for raspberry pi.

I had a screen and a raspberry lying around and I did not have a clock.
Here is one. With wttr.in weather forecast.

### Installation

`sudo apt install arp-scan`

`pip3 install termcolor pyfiglet pytz`

`pyfiglet -L dohmonosq.flf`
`pyfiglet -L bannerf.flf`

Place your script somewhere, like under `/home/pi/py-clock`

Add a crontab with `crontab -e`: mind the default output being `tty1`

`* * * * * python3 /home/pi/pyclock/clock.py > /dev/tty1 2>&1`
`* * * * * python3 /home/pi/pyclock/arp_list.py > /dev/tty1 2>&1`

Add the local network scanner to your `sudo crontab -e` as network scanning requires `sudo`

For name resolution edit `arp_list.py` as for some reason
I could not get that to work dynamically.

Create a `weather/location.txt` for the weather query.

Check it with wttr.in with curl:

`curl 'wttr.in/:help'`

If you want to hide the cursor, add `vt.global_cursor_default=0` to `cmdline.txt`

Enjoy!

### Other, better software

It does not support fyglets though.

https://github.com/wtfutil/wtf


MIT