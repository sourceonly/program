#!/usr/bin/python
from multiprocessing import Process, Queue
from multiprocessing.managers import BaseManager
import subprocess

import socket
import time
import copy

import config

conf=config.config('config')
server=conf.get_value('server')
port=int(conf.get_value('port'))
authkey=conf.get_value('authkey')
maxcpus=int(conf.get_value('maxcpus'))

res={'maxcpus':maxcpus,'usedcpus':0}


class QueueManager(BaseManager): 	pass;

QueueManager.register('get_queue_buffer')
QueueManager.register('get_queue_in'    )
QueueManager.register('get_queue_re'    )
QueueManager.register('get_queue_queue' )
QueueManager.register('get_queue_del'   )
QueueManager.register('get_queue_mess'  )
QueueManager.register('get_res'         )
QueueManager.register('get_jobid'       )


class pycli(): 
	def __init__(self,server,port,authkey,res): 
		self.m=QueueManager(address=(server,port),authkey=authkey);
		m=self.m
		m.connect();	
		self.plist={};
		self.q_bu=m.get_queue_buffer();
		self.q_re=m.get_queue_re();
		self.q_del=m.get_queue_del();
		self.q_mess=m.get_queue_mess();
		self.res_s=m.get_res()

		self.hostname=socket.gethostname()
		self.res=res.copy();
	def send_message(self,jobid,dict): 
		info={}
		info[jobid]=dict.copy()
		self.q_mess.put(info)
	
	def report_res(self): 
		self.res_s.update({self.hostname:self.res})
		
	def update_res(self): 
		used_cpus=0
		for i in self.plist: 
			used_cpus+=self.plist[i]['cpus']
		
		self.res['usedcpus'] = used_cpus
			

	def update_plist(self):
		for i in self.plist.keys(): 
			i.poll()
			jobid=self.plist[i]['jobid']
			jobbody=self.plist[i]
			jobbody['pid']=i.pid;
			jobbody['node']=self.hostname
			if i.poll() ==None	:
				jobbody['status']='Running'
				pass
			elif type(i.poll())==type(1)  	:
				jobbody['status']='Finished'
				jobbody['endtime']=time.time()
				self.plist.pop(i)
			self.send_message(jobid,jobbody);
				
	def try_del(self): 
		if self.q_del.empty():
			return 
		j=self.q_del.get()
		for i in self.plist: 
			if self.plist[i]['jobid']==j:
				i.terminate()
				return 
		self.q_del.put(j);	
		
			
	def run_task(self,job): 
		pc=subprocess.Popen(job['cmd'],shell=True)
		job['starttime']=time.time()
		job['status']='Running'
		job['pid']=pc.pid
		self.send_message(job['jobid'],job)
		self.plist[pc]=job
		return pc		
	def is_runable(self,job): 
		self.update_res()
		if int(job['cpus'])> self.res['maxcpus']-self.res['usedcpus']: 
			return False
		return True
	
	def try_run(self): 
		if self.q_bu.empty(): 
			return 
		job=self.q_bu.get();
		if self.is_runable(job): 
			self.run_task(job);
			
		else: 
			self.q_re.put(job);
			

			
	def serv_forever(self): 
		while True:
			print self.plist
			print self.res
	
			self.try_del()
			self.update_plist()
			self.try_run()
			self.update_res()	
			self.report_res()
			time.sleep(0.1);

a=pycli(server,port,authkey,res);
a.serv_forever()
