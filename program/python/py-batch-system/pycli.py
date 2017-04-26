#!/usr/bin/python
from multiprocessing import Process, Queue
from multiprocessing.managers import BaseManager
import subprocess
import os
import sys
import gc

import socket
import time
import copy

import config
cwd=os.path.abspath(os.path.dirname(sys.argv[0]))
os.environ['PATH']=os.path.join(cwd,'commands')+os.pathsep+os.environ['PATH']


conf=config.config('config')
server=conf.get_value('server')
port=int(conf.get_value('port'))
authkey=conf.get_value('authkey')
maxcpus=int(conf.get_value('maxcpus'))
sched_cycle=float(conf.get_value('sched_cycle'))
working_dir=(conf.get_value('working_dir'))
custom_resource=(conf.get_value_list('customres'));
res={'maxcpus':maxcpus,'usedcpus':0}

if custom_resource:
        for i in custom_resource:
                try:
                        res[i]=eval(conf.get_value(i));
                except:
                        res[i]=conf.get_value(i);


        for i in custom_resource:
                if type(res[i]) == type(1):
                        res['max'+i]=res[i];
                        res['used'+i]=0;

# res['group']=group;

class QueueManager(BaseManager): 	pass;

QueueManager.register('get_queue_buffer')
QueueManager.register('get_queue_in'    )
QueueManager.register('get_queue_queue' )
QueueManager.register('get_queue_del'   )
QueueManager.register('get_queue_mess'  )
QueueManager.register('get_res'         )
QueueManager.register('get_jobid'       )


class pycli(): 
        def __init__(self,server,port,authkey,res): 
                self.server=server
                self.port=port
                self.authkey=authkey
                self.res=res
                self.m=QueueManager(address=(server,port),authkey=authkey);
                self.custom_resource=custom_resource;
                self.__connect_init__();
	def __connect_init__(self):
		m=self.m
		m.connect();	
		self.plist={};
		self.q_bu=m.get_queue_buffer();
		self.q_del=m.get_queue_del();
		self.q_qu=m.get_queue_queue();
		self.q_mess=m.get_queue_mess();
		self.res_s=m.get_res()

		self.hostname=socket.gethostname()
		self.res=res.copy();
                # print self.res
                # self.update_res();
        def get_connect_status(self): 
                m=self.m
                return self.m._state.value
                
	def send_message(self,jobid,dict): 
		info={}
		info[jobid]=dict.copy()
		self.q_mess.put({'updatejob':info})
	
	def report_res(self): 
		self.res_s.update({self.hostname:self.res})
		
	def update_res(self): 
		used_cpus=0
		for i in self.plist: 
			used_cpus+=self.plist[i]['cpus']
		self.res['usedcpus'] = used_cpus
            
                for j in self.custom_resource:
                        if type(self.res[j])!=type(1):
                                continue
                        used_res=0;
                        for i in self.plist:
                                used_res+=self.plist[i][j];
                        self.res['used'+j]=used_res;
			

	def update_plist(self):
                # print 'in_update',self.plist
                finish_list=[];
		for i in self.plist.keys():

			j_status=i.poll()
			jobid=self.plist[i]['jobid']
			jobbody=self.plist[i]
			jobbody['pid']=i.pid;
			jobbody['node']=self.hostname
			if j_status ==None	:
				jobbody['status']='Running'
				pass
			elif type(j_status)==type(1)  	:
                                if j_status==0:
                                        jobbody['status']='Finished'
                                elif j_status==1: 
                                        jobbody['status']='Deleted'
                                else :
                                        jobbody['status']='Aborted'

                                jobbody['Exit_Status']=j_status;
				jobbody['endtime']=time.time()
                                self.send_message(jobid,jobbody);
                                finish_list.append(i);

                for i in finish_list:
		        self.plist.pop(i);

				
	def try_del(self): 
		if self.q_del.empty():
			return 
		j=self.q_del.get()
		for i in self.plist: 
			if self.plist[i]['jobid']==j:
				i.terminate();
				return 
		self.q_del.put(j);	
		
			
	def run_task(self,job): 
                j_dir=os.path.join(working_dir,str(job['jobid']))
                if not os.path.isdir(j_dir):
                        os.makedirs(j_dir)
                # self.update_plist();
		pc=subprocess.Popen(job['cmd'],shell=True,cwd=j_dir,env={'PATH':os.environ['PATH']})
                # print os.environ['PATH']
                                    
		job['starttime']=time.time()
		job['status']='Running'
		job['pid']=pc.pid
		self.send_message(job['jobid'],job)
                
		self.plist[pc]=job
                print 'in run',self.plist;
                # self.update_plist();
		return pc		
	def is_runable(self,job):
		if int(job['cpus'])> self.res['maxcpus']-self.res['usedcpus']:
			return False
                # if job.has_key('group'):
                #         if self.res['group']!=job['group']:
                #                 return False;

                for i in self.res:
                        if not job.has_key(i):
                                continue
                        for i in self.custom_resource:
                                if type(self.res[i])==type(1):
                                        if int(job[i])>int(self.res['max'+i])-int(self.res['used'+i]):
                                                return False
                                if type(self.res[i])==type("abc"):
                                        if job[i]!=self.res[i]:
                                                return False
		return True
	
	def try_run(self): 
		if self.q_bu.empty(): 
			return 
		p,job=self.q_bu.get();
		if self.is_runable(job): 
			self.run_task(job);
		else: 
			self.q_qu.put((p,job));
                        time.sleep(0.1*sched_cycle);	
			
	def serv_forever(self): 
		while True:
                        print "plist",self.plist
			self.try_del()
			self.update_plist()
                        self.update_res()
                        self.report_res()
			self.try_run()
                        self.update_res()	
                        self.update_plist()
			self.update_res()	
			self.report_res()
                        gc.collect()
			time.sleep(sched_cycle);


import gc

# a=pycli(server,port,authkey,res);
# a.serv_forever()

while True:
        try:
                a=pycli(server,port,authkey,res);
                a.serv_forever()
        except:
                pass
        gc.collect();
