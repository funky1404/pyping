#-*- coding: utf-8 -*-

import os
import platform
from datetime import datetime

net = raw_input("Enter the Network Address")
net1 = net.split('.')
a='.'

net2 = net1[0]+a+net1[1]+a+net1[2]+a
st1 = int(raw_input("Enter the Starting Number"))
en1 = int(raw_input("Enter the Last Number"))
en1 = en1 + 1
oper = platform.system()

if ( oper == "Windows") :
	ping1 = "ping -n 1 -t 1 "
elif ( oper == "Linux") :
	ping1 = "ping -c 1 -t 1 "
else : 
	ping1 = "ping -c 1 -t 1 "

t1 = datetime.now()
print "Scanning in Progress"

for ip in xrange(st1, en1):
	addr = net2 + str(ip)
	comm = ping1 + addr
	# print comm
	response = os.popen(comm)
	check = 0
	for line in response.readlines():
		# print line
		if(line.count("ttl")):
			check = 1
			# print addr,
			break
	if(check == 1):
		print addr, "--> Live"

t2 = datetime.now()
total = t2 - t1
print "Scanning complete in ", total