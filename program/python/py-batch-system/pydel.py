#!/usr/bin/python



from multiprocessing.managers import BaseManager
from multiprocessing import Queue


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


q=m.get_queue_del()

import sys
q.put(int(sys.argv[1]))




