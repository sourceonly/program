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
import worker
import multiprocessing as mp
if __name__=="__main__":
    while True: 
        current=fd.accept()
        cw=worker.sock_stream(current);
        cw.recvall();
        print pickle.loads(cw.stream)

    

    







