#!/usr/bin/python
from multiprocessing import Process, Queue
from multiprocessing.managers import BaseManager
import sys
import subprocess

import config

conf=config.config('config')
server=conf.get_value('server')
port=int(conf.get_value('port'))
authkey=conf.get_value('authkey')
	
class QueueManager(BaseManager): pass


QueueManager.register('get_queue_buffer')
QueueManager.register('get_queue_in'    )
QueueManager.register('get_queue_re'    )
QueueManager.register('get_queue_queue' )
QueueManager.register('get_queue_del'   )
QueueManager.register('get_res'         )
QueueManager.register('get_jobid'       )
QueueManager.register('get_joblist'     )







m=QueueManager(address=(server,port),authkey=authkey)

m.connect()
if __name__=="__main__":
	q=m.get_joblist();
	p=q.__deepcopy__(10);
        
        id_list=sys.argv[1:];


        key_list=[]
        if len(id_list)==0:
                key_list=p.keys();
        else:
                for i in id_list:
                        id=int(i);
                        if id in p.keys():
                                key_list.append(id);

        for i in key_list:
        
		print "jobid:",i
		keys=p[i].keys()
		keys.sort()
		for j in keys:
			
			print "\t%s=%s" % (str(j),str(p[i][j]))
		
