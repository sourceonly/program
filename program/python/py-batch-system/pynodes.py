#!/usr/bin/python



from multiprocessing.managers import BaseManager
from multiprocessing import Queue



import config

conf=config.config('config')
server=conf.get_value('server')
port=int(conf.get_value('port'))
authkey=conf.get_value('authkey')



class QueueManager(BaseManager): pass
QueueManager.register('get_queue_sub')
QueueManager.register('get_res')
m=QueueManager(address=(server,port),authkey=authkey)
m.connect()


q=m.get_queue_sub()
res=m.get_res();
nodes=res.__deepcopy__(1)


for i in nodes : 
	if i=='jobid':
		continue
	
	print "%s" % i
	print "\t%10s=%10s" % ('cpus',str(nodes[i]))
	

