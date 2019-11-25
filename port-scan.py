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

# Enter a website address or specific IP you wish to scan
HOST = input('[>>] Enter target IP: ') 

class PortScanner:
    def __init__(self, address, port):
        self.port = port 
        self.address = address

    def scan_port(self, port):
        s = socket.socket()
        try:
            s.connect((HOST, port))
            s.close()
            return True
        except:
            return False

for i in range(1024):
    scanner = PortScanner(HOST, i)
    if scanner.scan_port(i):
        cprint.info('{} [+] connection successful'.format(i) )
