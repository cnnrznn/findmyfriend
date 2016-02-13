#!/usr/bin/python

# This is a UDP client for testing the FindMyFriend
# server.

import socket

_host = ""
_tcp_port = 1232
_udp_port = 1233
_inf_port = 1235
_loc_port = 1234

udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_sock.bind((_host, _udp_port))

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.bind((_host, _tcp_port))

# TODO send device requests
# TODO send channel requests
# TODO send device location
