#!/usr/bin/python

import socket


HOST = ''
PORT = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

print("Connected by {}".format(addr))
conn.close()
