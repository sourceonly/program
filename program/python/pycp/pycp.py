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

content=""
while True: 
	rc=sd.recv(1024);
	if not rc: 
		break
	content+=rc
#	print rc
	

f=open(locate,'wb')
f.write(content)
f.close()


