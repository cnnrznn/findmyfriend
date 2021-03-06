#!/usr/bin/python

# This is a simple server program to facilitate the communication
# of the FindMyFriend application.

import socket

### FUNCTIONS ###

def construct_message(addr):
    message = ""
    message += addrs[addr][1]
    message += ","
    message += addrs[addr][2]
    return message

### SCRIPT ###

# TODO incorporate argparse
# debugging flag (write to stderr)

_req_dev_id = -1
_req_chan_id = -2
_req_disconnect = -3

_host = ""
_loc_port = 1234 # port for handling UDP location updates
_inf_port = 1235 # port for handling TCP information exchange (device id, channel)

# port for location data
loc_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
loc_sock.bind((_host, _loc_port))
loc_sock.settimeout(0.01)
_loc_data_size = 195

# port for information data
inf_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
inf_sock.bind((_host, _inf_port))
inf_sock.settimeout(0.01)
inf_sock.listen(5)
_inf_data_size = 65

channels = dict()   # {chan_id, [dev_id1, dev_id2]}
devs = dict()       # {dev_id, [chan_id, lat, lon]}

next_channel = 0 # TODO randomize
next_device = 0 # TODO randomize

while True:
    try:
        tmp_sock, tmp_addr = inf_sock.accept()
        tmp_sock.setblocking(0) # so malicious app's don't 'stall' server
        req = int(tmp_sock.recv(_inf_data_size).split(',')[0])

        if req == _req_dev_id:             # issue a device id
            devs[next_device] = [-1, -1, -1]
            tmp_sock.send(str(next_device) + ",")
            next_device += 1 # TODO randomize
        elif req == _req_chan_id:          # issue a channel id
            dev_id = int(tmp_sock.recv(_inf_data_size).split(",")[0])
            channels[next_channel] = [dev_id, None]
            devs[dev_id][0] = next_channel
            tmp_sock.send(str(next_channel) + ",")
            next_channel += 1 # TODO randomize
        elif req == _req_disconnect:       # free the device id and possibly the channel id
            dev_id = int(tmp_sock.recv(_inf_data_size).split(',')[0])
            chan_id = devs[dev_id][0]
            del devs[dev_id]
            if chan_id in channels:
                if channels[chan_id][1] == None:    # this device is the last in the channel
                    del channels[chan_id]
                else:                               # this device is the first to leave
                    if channels[chan_id][0] == dev_id:
                        channels[chan_id][0] = channels[chan_id][1]
                    channels[chan_id][1] = None

        print "next_device:", next_device
        print "next_channel:", next_channel
        print "devs:", devs
        print "channels:", channels
        print

        tmp_sock.close()
    except socket.timeout:
        # do nothing
        pass

    try:
        data, tmp_addr = loc_sock.recvfrom(_loc_data_size)

        # extract data from packet
        data = data.split(',')
        lat = float(data[0])
        lon = float(data[1])
        dev_id = int(data[2])

        # respond with the relevent location

        # TODO debugging location
        sock.sendto("39.677501,-75.75207", tmp_addr)
        """
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
        """

        print "Location from", tmp_addr
        print "dev_id:", dev_id, type(dev_id)
        print "lat:", lat, type(lat)
        print "lon:", lon, type(lon)
        print

        # DEBUG print dictionaries
        print channels
        print devs
        print

    except socket.timeout:
        # do nothing
        pass
