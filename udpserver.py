#!/usr/bin/python

# This is a simple udp server to support communication with
# with the FindMyFriend application.
#
# Currently, it replies with the hard-coded coordinates of the
# fountain on UD's south green.

import socket
import struct

### FUNCTIONS ###

def construct_message(addr):
    message = ""
    message += addrs[addr][1]
    message += ","
    message += addrs[addr][2]
    return message

### SCRIPT ###

_host = ""
_port = 1234

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((_host, _port))

channels = dict()
addrs = dict()

next_channel = 0

while True:
    data, addr = sock.recvfrom(256)

    # extract data from packet
    reqid = data[2]
    reqlat = data[0]
    reqlon = data[1]

    if reqid < 0:
        if addr in addrs:
            # resend assigned channel number
            sock.sendto(addrs[addr][0], addr)
        else:
            # assign new channel number
            addrs[addr] = [next_channel, -1, -1]
            channels[next_channel] = [addr, None]
            next_channel += 1
    else:
        # respond with the relevent location
        #sock.sendto("39.677501,-75.75207", addr)
        if addr in addrs:
            # respond with the other addr's location
            possaddrs = channels[reqid]
            message = ""
            if addr == possaddrs[0]:
                message = construct_message(possaddrs[1])
            else:
                message = construct_message(possaddrs[0])
            sock.sendto(message, addr)
            # update this addr's location
            addrs[addr][1] = reqlat
            addrs[addr[2] = reqlon
        elif channels[reqid][1] == None:
            # TODO join this addr to the connection
        else:
            # ignore request
            pass

    # print information about request
    print "Packet from", addr
    data = data.split(',')
    data[2] = struct.unpack(">I", data[2])[0]
    print "Data"
    for i in xrange(3):
        print data[i]

    print ""

    # DEBUG print dictionaries
    print channels
    print addrs
