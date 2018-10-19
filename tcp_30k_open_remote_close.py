#!/usr/bin/python

import socket
import sys
import struct
import time
import array

loops = 0
print("Starting testing...")
while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    l_onoff = 1
    l_linger = 1
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', l_onoff, l_linger))
    print("connecting socket loop {}".format(loops))
    notConnected = True
    while notConnected:
        try:
            sock.connect(('10.0.4.200', 5555))
            notConnected = False
        except socket.error as msg:
            time.sleep(.25)
    temp = sock.recv(10)
    sock.close()
    loops = loops + 1
    if loops > 30000000:
        time.sleep(1)
        loops = 0
        print("Exiting after {} open/closes".format(loops))
        break
