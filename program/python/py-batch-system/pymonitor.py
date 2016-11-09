#!/usr/bin/python

from multiprocessing.managers import BaseManager
from multiprocessing import Queue
import config

conf=config.config('config')
server=conf.get_value('server')
port=int(conf.get_value('port'))
authkey=conf.get_value('authkey')



class QueueManager(BaseManager): pass


QueueManager.register('get_queue')
QueueManager.register('get_queue_sub')
QueueManager.register('get_jobs')

m=QueueManager(address=(server,port),authkey=authkey)
m.connect();


while True:
	l=m.get_jobs()
	q1=m.get_queue()
	q2=m.get_queue_sub()
	while not q2.empty() and  not q1.full():
		j=q2.get()
		k=j.copy()
		l.update({k['jobid']:k})
		q1.put(j)



	




