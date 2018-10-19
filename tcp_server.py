#!/usr/bin/python

import socket


HOST = ''
PORT = 43690

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

print("Connected by {}".format(addr))
conn.close()
