#!/usr/bin/python

# This server issues device id's

import socket

_host = ""
_port = 1235

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((_host, _port))

sock.listen(5)

while True:
    tmp_sock, addr = sock.accept()

    # TODO receive operation (request, free)
    # TODO perform operation

    tmp_sock.close()
