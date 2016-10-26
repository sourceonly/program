import os
import sys
port=int(sys.argv[1])
server='localhost'

buffsize=1024
addr=(server,port)

from socket import *

fd=socket(AF_INET,SOCK_STREAM,0);

fd.bind(addr);
import pickle
fd.listen(5);

while True: 
    current=fd.accept();
    curr_connect=current[0]
    s=curr_connect.recv(buffsize) 
    stream=s
    while s :
        s=curr_connect.recv(buffsize) 
        stream+=s; 
    curr_connect.close()
    print stream
    print '---'
    value=pickle.loads(stream);
    filename=os.path.join("/tmp",os.path.basename(value["filename"]));
    f=open(filename,"w")
    f.write(value['body'])
    f.close()
    







