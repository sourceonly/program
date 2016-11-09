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
jobid=res.__deepcopy__(1)['jobid']
res.update({'jobid':jobid+1})


print jobid

job={}
job['jobname']='ABC'
job['jobid']=jobid
job['cpus']=2
job['cmd']='dir'
q.put(job)






