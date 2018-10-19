#!/usr/bin/python

import socket
import sys
import struct
import time
import array

data = [[x] * 256 for x in xrange(0,2000)]
b = []
for x in data:
    b = b + x
output = array.array('L', b).tostring()

#counter = 6000
#counter = 300200000
#counter = 1500000
counter = 0
loops = 0
#while counter < 300200000:
print("Starting testing...")
while True:
#    print("creating socket {}".format(counter))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    l_onoff = 1
    l_linger = 1
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', l_onoff, l_linger))
    print("connecting socket loop {}".format(loops))
    notConnected = True
    out_data = output[0:counter+1]
    while notConnected:
        try:
            sock.connect(('10.0.4.200', 5555))
            #sock.connect(('10.0.2.14', 5555))
            notConnected = False
        except socket.error as msg:
            time.sleep(.25)
    remaining = len(out_data)
    tx_out = 0
    tx_limit = 0
    result = ""
    while remaining != 0:
        if (tx_out+1460) > len(out_data):
            tx_limit = len(out_data)
        else:
            tx_limit = tx_out + 1460
        sock.sendall(out_data[tx_out:tx_limit])
        tx_out = tx_limit
        tmprem = 0
        if remaining < 1460:
            tmprem = remaining
        else:
            tmprem = 1460
        temp = sock.recv(tmprem)
        remaining = remaining - len(temp)
#chk        result = "".join([result,temp])
#        print("Loopback data received, {} bytes remaining").format(remaining)
#chk    if (out_data == result):
#chk        testvar = 0
#        print("Data match len {} bytes".format(counter+1))
#chk     else:
#chk        print(">>>>>Data mismatch<<<<< {} bytes".format(counter+1))
#    while True:
#        time.sleep(1)
    sock.close()
#    time.sleep(3)
#    print("socket closed")
    loops = loops + 1
    if loops > 30000:
        time.sleep(1)
        loops = 0
#        print("Restarting next loop interation.")
        print("Exiting after {} open/closes".format(loops))
        break
#    counter = counter + 10000
#    break
