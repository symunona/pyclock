# List computers on network

from terminal import clear
import subprocess
import shlex

INTERFACE_NAME = 'wlan0'

familiar = {
    # 'mac address': 'name to be resolved to'
}

class NetworkComputer:
    def __init__(self, ip, mac, name):
        self.ip = ip
        self.mac = mac
        self.name = name
        self.resolve = familiar.get(self.mac) or ''



def getUsersOnSubnet():
    outputRaw = subprocess.check_output(shlex.split('arp-scan -I ' + INTERFACE_NAME + ' -l'))
    output = outputRaw.splitlines()
    users = {}
    for device in output[2:-3]:
        line_parts = device.decode().split('\t')
        ip = line_parts[0]
        users[ip] = (NetworkComputer(ip, line_parts[1], line_parts[2]))
    return users

def printUsers():
    users = getUsersOnSubnet().values()
    clear(57, 0, 12, 40)
    for user in users:
        print(user.ip + ' ' + user.resolve )



printUsers()
