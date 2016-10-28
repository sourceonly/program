#!/bin/env python

import sys 

port=9010
addr=sys.argv[1]
rlocate=sys.argv[2]
locate=sys.argv[3]

from socket import * 

sd=socket(AF_INET,SOCK_STREAM,0);
sd.connect((addr,port));

sd.send(rlocate);

f=open(locate,'wba')
while True: 
	rc=sd.recv(1024);
	if not rc: 
		break
	f.write(rc)
#	print rc
	

f.close()


