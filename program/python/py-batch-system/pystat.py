from multiprocessing import Process, Queue
from multiprocessing.managers import BaseManager
import subprocess

import config

conf=config.config('config')
server=conf.get_value('server')
port=int(conf.get_value('port'))
authkey=conf.get_value('authkey')

	
class QueueManager(BaseManager): pass

QueueManager.register('get_queue')
QueueManager.register('get_jobs')
QueueManager.register('get_res')
m=QueueManager(address=(server,port),authkey=authkey)

m.connect()
if __name__=="__main__":
	q=m.get_jobs();
	p=q.__deepcopy__(1);
	for i in p:
		print "jobid:",i
		for j in p[i]: 
			print "\t%s=%s" % (str(j),str(p[i][j]))
		
		
	res=m.get_res()
