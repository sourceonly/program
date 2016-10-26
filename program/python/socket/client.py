
import socket 
import pickle

import sys
port=int(sys.argv[1])
fd=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0);

addr=("localhost",port);

fd.connect(addr);
dict={'filename':'/etc/passwd'}
f=open(dict['filename'],'rb')
dict['body']=f.read()
f.close()
fd.sendall(pickle.dumps(dict))
fd.close()

