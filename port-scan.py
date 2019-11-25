#!/usr/bin/env python3

import socket 
import subprocess

try:
    from cprint import * 
except:
    import sys 
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'cprint'])

# Set our variables
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = input('[+] Enter target IP: ')
DEFAULT_TIMEOUT = 0.5

class PortScanner:
    def __init__(self, port, address):
        self.port = port 
        self.address = address

    def scan_port(self, port):
        s = socket.socket()
        try:
            s.connect((HOST, port))
            return True
        except:
            return False

for i in range(444):
    scanner = PortScanner(i, HOST)
    if scanner.scan_port(i):
        cprint.info('%d [+] connection successful' % (i) )
        s.close()




    