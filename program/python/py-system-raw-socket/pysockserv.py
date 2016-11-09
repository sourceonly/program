import time
import pyprocess
import pymessage
import multiprocessing
import select
from socket import *
from node import pynode
import json


class pyserv(multiprocessing.Process): 
	def __init__(self,addr,port):
		self.mp=multiprocessing.Process()
		self.buffersize=1024
		self.read={}
		self.write={}
		self.file_queue={}
		self.task_queue={}
		self.dispatcher=pyprocess.dataprocess();
		self.encoder=pymessage.json_message()
		self.sd_read=[]
		self.sd_write=[]
		self.sd_err=[]
		self.addr=(addr,port)
		self.sd=None;
		self.init_serv()
		self.status={};
		self.node=pynode.pynode()
		self.init_dispatcher()
	def query(self,dict_body): 
		return self.encoder.encode('qres',self.node.report())
	
	def route(self,dict_body):
		route=dict_body['route']
		print 'route to ', route
		sd=socket(AF_INET,SOCK_STREAM,0)	
		sd.connect((route[0],route[1]))
		sd.sendall(json.dumps(dict_body['body']))
		sd.setblocking(False)
		try:
			res=sd.recv(1024);
		except:
			res='no value'
		sd.close()
		return 'routed'
		
	def submit(self,dict_body): 
		cmd=dict_body['cmd']
		fileo=dict_body['fileo']
		self.node.add_tasks(cmd,fileo);
		return 'success'
			
		
		
	def init_dispatcher(self): 	
		self.dispatcher.register('query',self.query)
		self.dispatcher.register('submit',self.submit)	
		self.dispatcher.register('route',self.route)	
		
	def init_serv(self):
		self.sd=socket(AF_INET,SOCK_STREAM,0);
		sd=self.sd;
		self.sd_read.append(sd);
		addr=self.addr;
		sd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
		sd.bind(addr);
		sd.setblocking(False)
		sd.listen(5)	
	def append_s_fd(self,fd): 
		if not fd in self.sd_read: 
			self.sd_read.append(fd)
	def append_w_fd(self,fd):
		if not fd in self.sd_write:
			self.sd_write.append(fd)
	def remove_fd(self,fd):
		if fd in self.sd_read: 
			self.sd_read.remove(fd)
		if fd in self.sd_write:
			self.sd_write.remove(fd)
		if fd in self.sd_err: 
			self.sd_err.remove(fd)
		
	def accept(self,fd): 
		if not fd==self.sd:		 
			return 
		conn,addr=self.sd.accept()

		return conn
	def serv(self):
		while True:
			#time.sleep(1)
			#print time.time()
			r,w,e=select.select(self.sd_read,self.sd_write,self.sd_err,1)
			for i in r: 
				if i == self.sd: 
					conn,addr=self.sd.accept();
					self.read[conn]={}
					self.read[conn]['level']=0
					self.read[conn]['content']=''
					self.sd_read.append(conn)
					self.sd_write.append(conn)
					self.task_queue[conn]=multiprocessing.Queue();
					self.write[conn]=multiprocessing.Queue();
					conn.setblocking(False)
				else:
					try: 
						buf=i.recv(self.buffersize);
					except: 
						buf=''
						
					for c in range(len(buf)):
						if buf[c]== '{':
							self.read[i]['level']+=1
						elif buf[c]=='}' :
							self.read[i]['level']-=1
						self.read[i]['content']+=buf[c]
						if self.read[i]['level']==0 :
							if self.read[i]['content']!='':
								self.task_queue[i].put(self.read[i]['content']);
								self.read[i]['content']=''
						
			#		self.sd_read.remove(i)
					if not i in self.sd_write:
						self.sd_write.append(j)	
					
			for l in self.task_queue.keys():
				while not self.task_queue[l].empty():
					info=self.task_queue[l].get_nowait()
					#print info	
					if info:
						header=self.encoder.get_header(info);
						body=self.encoder.get_body(info);	
						res=self.dispatcher.dispatcher(header,(body,));
						print res
						self.write[l].put(self.encoder.encode('qres',res));
			for j in w: 
				if j in self.write.keys():
					while not self.write[j].empty():
						info=self.write[j].get_nowait()
						if info:
							try: 
								j.sendall(info);
							except: 
								print 'send err'

				#	self.sd_write.remove(j)
					if not j in self.sd_read:
						self.sd_read.append(j)
							
			for k in e: 
				print k	

			self.node.update()
	
if __name__=='__main__':
	import sys
	port=int(sys.argv[1])
	a=pyserv('',port)
	a.serv()
