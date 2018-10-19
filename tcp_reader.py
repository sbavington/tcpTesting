#!/usr/bin/python

import socket
import sys
import struct
import time
import array


print("creating socket")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
l_onoff = 1
l_linger = 1
sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', l_onoff, l_linger))
print("connecting socket")
notConnected = True
while notConnected:
    try:
        sock.connect(('10.0.4.200', 5555))
        notConnected = False
    except socket.error as msg:
        time.sleep(.25)
# Send the file name to pull in
fileName = "0"
print("Fetching file object {}".format("0"))
sock.sendall(fileName)
print("Opening file {} for writing".format("sampleFile"))
with open("sampleFile", "w") as outfile:
    result = ""
    tmprem = 32768 
    while True:
        temp = sock.recv(tmprem)
        if not temp:
            break
        outfile.write(temp)
    print("file closed")
sock.close()
print("socket closed")
