#!/usr/bin/python

# This is a UDP client for testing the FindMyFriend
# server.

_host = ""
_port = 1235

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((_host, _port))

# TODO send device requests
# TODO send channel requests
# TODO send device location
