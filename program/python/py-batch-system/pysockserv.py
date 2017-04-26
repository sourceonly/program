#!/usr/bin/python
from multiprocessing import Process, Queue
import multiprocessing as mp
from multiprocessing.managers import BaseManager
import Queue
import config

conf=config.config('config')
server=conf.get_value('server')
port=int(conf.get_value('port'))
authkey=conf.get_value('authkey')
sched_buffer=int(conf.get_value('sched_buffer'))
sched_cycle=float(conf.get_value('sched_cycle'))

queue_in=mp.Queue();

queue_buffer=Queue.PriorityQueue(sched_buffer);
queue_queue=Queue.PriorityQueue();


queue_del=mp.Queue();
queue_mess=mp.Queue();

res  = {} ;
jobid = {'jobid':1};
joblist={};


class QueueManager(BaseManager): pass
    

QueueManager.register('get_queue_buffer',        callable=lambda: queue_buffer)
QueueManager.register('get_queue_in'    ,        callable=lambda: queue_in    )
QueueManager.register('get_queue_queue' ,        callable=lambda: queue_queue )
QueueManager.register('get_queue_del'   ,        callable=lambda: queue_del   )
QueueManager.register('get_queue_mess'  ,        callable=lambda: queue_mess  )
QueueManager.register('get_res'         ,        callable=lambda: res 	      )
QueueManager.register('get_jobid'       ,        callable=lambda: jobid       )
QueueManager.register('get_joblist'     ,        callable=lambda: joblist     )




import time

m = QueueManager(address=(server, port), authkey=authkey)
s=m.get_server()
s.serve_forever();





# import threading
# t=threading.Thread(target=s.serve_forever,args=())
# t.start()
# t.join();




    
# s = m.get_server()
# s.serve_forever()




