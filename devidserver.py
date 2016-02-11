#!/usr/bin/python

# This server issues device id's

import socket

_req_devid = -1
_free_devid = -2

_host = ""
_port = 1235

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((_host, _port))

sock.listen(5)

while True:
    tmp_sock, addr = sock.accept()

    # receive operation (request, free)
    req = int(tmp_sock.recv(1))

    # TODO perform operation
    if req == _req_devid:
        pass
    elif req == _free_devid:
        pass

    tmp_sock.close()
