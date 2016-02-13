#!/usr/bin/python

# This is a simple udp server to support communication with
# with the FindMyFriend application.

import socket
import sys

### FUNCTIONS ###

def construct_message(addr):
    message = ""
    message += addrs[addr][1]
    message += ","
    message += addrs[addr][2]
    return message

### SCRIPT ###

_req_devid = -1
_req_chanid = -2
_req_disconnect = -3

_host = ""
_loc_port = 1234 # port for handling UDP location updates
_inf_port = 1235 # port for handling TCP information exchange (device id, channel)

loc_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
loc_sock.bind((_host, _loc_port))
loc_sock.settimeout(0.01)

inf_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
inf_sock.bind((_host, _inf_port))
inf_sock.settimeout(0.01)
inf_sock.listen(5)

channels = dict()   # {chan_id, (dev_id1, dev_id2)}
devs = dict()       # {dev_id, (chan_id, lat, lon)}

next_channel = 0
next_device = 0

while True:
    try:
        tmp_sock, tmp_addr = inf_sock.accept()
        data = int(tmp_sock.recv(1))

        if data == _req_devid:
            # TODO issue a device id
            pass
        elif data == _req_chanid:
            # TODO issue a channel id
            pass
        elif data == _req_disconnect:
            # TODO free the device id and possibly
            # the channel id
            pass

        tmp_sock.close()
    except socket.timeout:
        # do nothing
        pass

    try:
        data, addr = loc_sock.recvfrom(256)

        # extract data from packet
        data = data.split(',')
        req_id = int(data[0])
        req_lat = float(data[1])
        req_lon = float(data[2])

        """
        if req_id < 0: # a request for id
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
                possaddrs = channels[req_id]
                message = ""
                if addr == possaddrs[0]:
                    message = construct_message(possaddrs[1])
                else:
                    message = construct_message(possaddrs[0])
                sock.sendto(message, addr)
                # update this addr's location
                addrs[addr][1] = req_lat
                addrs[addr][2] = req_lon
            elif channels[reqid][1] == None:
                # TODO join this addr to the connection
                pass
            else:
                # ignore request
                pass

        # print information about request
        print "Packet from", addr
        data[2] = struct.unpack(">I", data[2])[0]
        print "Data"
        for i in xrange(3):
            print data[i]

        print
        """

        print "Request from", addr
        print "req_id:", req_id, type(req_id)
        print "req_lat:", req_lat, type(req_lat)
        print "req_lon:", req_lon, type(req_lon)
        print

        # DEBUG print dictionaries
        print channels
        print devs
        print

    except socket.timeout:
        # do nothing
        pass
