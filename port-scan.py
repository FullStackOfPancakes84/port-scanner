#!/usr/bin/env python3

import socket 
import subprocess

try:
    from cprint import * 
except:
    import sys 
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'cprint'])

def opening_message():
    quotes = "''"
    cprint.ok('When using a website address such as www.google.com, wrap the text in {}'.format(quotes))

opening_message()

# Set our variables
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
COUNT = 0

# Enter a website address or specific IP you wish to scan
HOST = input('[>>] Enter target IP: ') 

class PortScanner:
    def __init__(self, address, port):
        self.port = port 
        self.address = address

    # Attempt to connect to the port
    def scan_port(self, port):
        s = socket.socket()
        try:
            s.connect((HOST, port))
            s.close()
            return True
        except:
            return False

# Return count of open ports 
def return_count(address, count):
    cprint.warn('Scan of {} returned {} open ports'.format(address, count) )

if __name__ == '__main__':

    # Scan ports in range 
    for i in range(1024):
        scanner = PortScanner(HOST, i)

        # Did we find an open port?
        if scanner.scan_port(i):
            try: 
                service = socket.getservbyport(i)
            except:
                service = 'Unable to determine'
            COUNT += 1
            cprint.info('{} [+] connection successful. Service: {}'.format(i, service) )

    # Display the # of open ports
    return_count(HOST, COUNT)