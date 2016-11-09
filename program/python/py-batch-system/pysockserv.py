from multiprocessing import Process, Queue
from multiprocessing.managers import BaseManager
import config

conf=config.config('config')
server=conf.get_value('server')
port=int(conf.get_value('port'))
authkey=conf.get_value('authkey')

queue = Queue() 
queue_to_submit= Queue()
jobs={}
res={'jobid':1}

class QueueManager(BaseManager): pass

QueueManager.register('get_queue', callable=lambda: queue)
QueueManager.register('get_queue_sub', callable=lambda: queue_to_submit)
QueueManager.register('get_jobs', callable=lambda: jobs)
QueueManager.register('get_res',callable=lambda:res)

m = QueueManager(address=(server, port), authkey=authkey)
s = m.get_server()
s.serve_forever()
