# List computers on network

from terminal import clear, move
import subprocess
import shlex
import socket
import json
from os.path import  dirname, realpath

INTERFACE_NAME = 'wlan0'

familiar = {}
try:
    # 'mac address': 'name to be resolved to'
    familiar = json.load(open(dirname(realpath(__file__)) + '/arp.json', 'r'))
except:
    pass

class NetworkComputer:
    def __init__(self, ip, mac, name):
        self.ip = ip
        self.mac = mac
        self.name = name
        self.resolve = familiar.get(self.mac) or ''
        if (ip.endswith('50')): self.resolve = ' * panni (gateway)'


def network_status ():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        sock_ip = s.getsockname()[0] + ' * me'
        s.close()
        return sock_ip
    except:
        return "no network"


def getUsersOnSubnet():
    command = shlex.split('/usr/sbin/arp-scan -I ' + INTERFACE_NAME + ' -l')
    output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')

    output = output.splitlines()

    users = {}
    for device in output[2:-3]:
        line_parts = device.split('\t')
        ip = line_parts[0]
        users[ip] = (NetworkComputer(ip, line_parts[1], line_parts[2]))
    return users

def printUsers():
    status = network_status()
    clear(33, 0, 1, 50)
    print(status)

    users = getUsersOnSubnet().values()
    if (len(users) > 0):
        clear(35, 0, 10, 50)
        print('users:')
        for user in users:
            print(user.ip + ' ' + user.resolve )

printUsers()
