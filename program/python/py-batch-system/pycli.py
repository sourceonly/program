from multiprocessing import Process, Queue
from multiprocessing.managers import BaseManager
import subprocess

import socket
import time


import config

conf=config.config('config')
server=conf.get_value('server')
port=int(conf.get_value('port'))
authkey=conf.get_value('authkey')
maxcpus=int(conf.get_value('maxcpus'))

	
class QueueManager(BaseManager): pass

QueueManager.register('get_queue')
QueueManager.register('get_res')
QueueManager.register('get_jobs')


cp={}

m=QueueManager(address=(server,port),authkey=authkey)
m.connect()

current=maxcpus
q=m.get_queue()
job=m.get_jobs()
res=m.get_res();
hostname=socket.gethostname()
	
if __name__=="__main__":
	while True:
		
		current=maxcpus
		task_to_clean=[]
		for i in cp.keys(): 	
			cp[i]['job']['node']=hostname
			if i.poll()==None:
				current-=cp[i]['job']['cpus']
				cp[i]['job']['status']='Running'
				cp[i]['job']['pid']=i.pid
				job.update({cp[i]['job']['jobid']:cp[i]['job']})
			else:
				cp[i]['job']['status']='Finished'
				job.update({cp[i]['job']['jobid']:cp[i]['job']})
				cp.pop(i)
		res.update({hostname:current})
		while not q.empty():
			job_to_run=q.get()
			
			if job_to_run['cpus']>current: 
				q.put(job_to_run);
				continue
			res.update({hostname:(current-job_to_run['cpus'])})
			print res
			print job_to_run
			rc=subprocess.Popen(job_to_run['cmd'],shell=True);
			cp[rc]={}
			cp[rc]['job']=job_to_run
					
			
			time.sleep(0.1)
					
						
			
				
					
					




