#!/bin/env python

from socket import * 
from select import *
port=9010
addr='192.168.0.90'

sd=socket(AF_INET,SOCK_STREAM,0)
sd.bind((addr,port));
sd.listen(5);
sd.setblocking(0);

input=[sd];
output=[]
error=[]
pair=[];
while True:
	r,w,e=select(input,output,error,5);
	for i in r: 
		if i==sd: 
			conn,addr=i.accept()
			input.append(conn);	
			print  "recv req from %s" % addr[0]
		else:	
			filename=i.recv(1024);  # simply we assume the filename is no longer than 1024
			pair.append((filename,i,));
			input.remove(i);	
			output.append(i);
	for j in w: 
		for p in pair: 
			if j in p:
				to_send=p[1];
				file_to_send=p[0];
				break;
		try:
			fs=open(file_to_send,"rb");
			to_send.sendall(fs.read());
			fs.close()
		except:
			pass
		output.remove(j)
		pair.remove(p)
		j.close();
	for k in e: 
		pass


			
			
