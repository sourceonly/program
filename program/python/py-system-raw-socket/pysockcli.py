

from socket import * 
import json;

class pysockcli:
	def __init__(self,addr): 
		self.addr=addr	
		self.sd=socket(AF_INET,SOCK_STREAM,0)
		self.buffsize=1024
				
	
