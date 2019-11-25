#!/usr/bin/env python3

import socket 

def install(package):
    print('Installing %s' % package)
    subprocess.call([sys.executable, '-m', 'pip', 'install', package])

try:
    from cprint import * 
except:
    import subprocess
    import sys 
    install('cprint')
    


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = input('[+] Enter target IP: ')

DEFAULT_TIMEOUT = 0.5

def scan_port(port, timeout=DEFAULT_TIMEOUT):
    s = socket.socket()
    s.settimeout(timeout)
    try: 
        s.connect((HOST, port))
        return True
    except:
        return False

for i in range(1,100):
    if scan_port(i):
        cprint.info('%d [+] connection successful' % (i))
        s.close()

    