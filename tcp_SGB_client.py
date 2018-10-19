#!/usr/bin/python

import socket
import sys
import struct
import time
import array

data = [[x] * 256 for x in xrange(0,1000)]
b = []
for x in data:
    b = b + x
output = array.array('L', b).tostring()

counter = 2000
while counter < 3100000:
#while True:
    print("creating socket {}".format(counter))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    l_onoff = 1
    l_linger = 1
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', l_onoff, l_linger))
    print("connecting socket")
    notConnected = True
    out_data = output[0:counter+1]
    while notConnected:
        try:
            sock.connect(('10.0.2.2', 5555))
            sock.sendall(out_data)
            notConnected = False
        except socket.error as msg:
            time.sleep(.25)
    time.sleep(.025)
    remaining = len(out_data)
    result = ""
    counter = 1
    while remaining != 0:
        print counter
        counter = counter + 1
        temp = sock.recv(remaining)
        remaining = remaining - len(temp)
        result = "".join([result,temp])
        print("Loopback data received, {} bytes remaining").format(remaining)
    if (out_data == result):
        print("Data match len {} bytes".format(counter+1))
    else:
        print(">>>>>Data mismatch<<<<< {} bytes".format(counter+1))
#    while True:
#        time.sleep(1)
    sock.close()
    print("socket closed")
    counter = counter + 10
