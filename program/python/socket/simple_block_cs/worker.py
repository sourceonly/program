import socket
import pickle
class sock_stream () :
    def __init__(self, sock_accept_tuple): 
        self.buffer=1024
        self.sockfd=sock_accept_tuple[0];
        self.sockaddr=sock_accept_tuple[1];
        self.stream='';
    def recvall(self):
        while self.recv_once():
            pass
        return self.stream;
        
    def recv_once(self):
        s=self.sockfd.recv(self.buffer);
        if s:
            self.stream+=s;
        return s;
    
        
class worker(): 
    def __init__(self,dict): 
        self.dict=dict;
        
