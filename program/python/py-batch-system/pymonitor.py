#!/usr/bin/python
from multiprocessing.managers import BaseManager
from multiprocessing import Queue
import config
import time
import copy
import gc

conf=config.config('config')
server=conf.get_value('server')
port=int(conf.get_value('port'))
authkey=conf.get_value('authkey')
sched_cycle=float(conf.get_value('sched_cycle'))

class QueueManager(BaseManager): pass


QueueManager.register('get_queue_buffer')
QueueManager.register('get_queue_in'    )
QueueManager.register('get_queue_queue' )
QueueManager.register('get_queue_del'   )
QueueManager.register('get_res'         )
QueueManager.register('get_jobid'       )
QueueManager.register('get_joblist'     )
QueueManager.register('get_queue_mess'  )
QueueManager.register('get_server'      )

m=QueueManager(address=(server,port),authkey=authkey);
print dir(m);
# print m._number_of_objects()
# print m._number_of_objects
print m.__dict__
print m._Client()
m.connect();



q_in=m.get_queue_in()
q_qu=m.get_queue_queue()
q_bu=m.get_queue_buffer()
q_del=m.get_queue_del()	
q_mess=m.get_queue_mess()

job_list=m.get_joblist()

while True:
	# get q_in and then record
	while not q_in.empty(): 
		job=q_in.get();
		if job.has_key('priority'):
			priority=-int(job['priority'])
		else:
			priority=0;
		job_shadow=copy.deepcopy(job);
		job_list.update({job_shadow['jobid']:job_shadow});
		q_qu.put((priority,job))
        # do message
	while (not q_mess.empty()) :
		message=q_mess.get()
                print 'message',message
		for i in message: 
			j=message[i]
			if i=='updatejob':	
				for k in j :
					job_list.update({k:j[k]})
                time.sleep(0.1);
	
	# do sched 
	
        
	while (not q_qu.empty()) and (not q_bu.full()): 
		pjob=q_qu.get() ; 
		q_bu.put(pjob)  ; 
		# print pjob
					
        gc.collect()
	time.sleep(0.1)
