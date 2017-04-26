#!/usr/bin/python

from multiprocessing.managers import BaseManager
from multiprocessing import Queue


import config
conf=config.config('config')
server=conf.get_value('server')
port=int(conf.get_value('port'))
authkey=conf.get_value('authkey')



class QueueManager(BaseManager): pass


QueueManager.register('get_res')
m=QueueManager(address=(server,port),authkey=authkey)
m.connect()


res=m.get_res();
nodes=res.__deepcopy__(1)


for i in nodes : 
	print "%s" % i
	for j in nodes[i]:	
		print "\t%20s=%20s" % (j,nodes[i][j])
	

