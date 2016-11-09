#!/usr/bin/python

import Queue
class job_queue:
	def __init__(self): 
		self.queue=Queue.PriorityQueue()
	def add_task(self,p,t):
		self.queue.put((p,t))
	def get_nexttask(self):
		return self.queue.get_nowait()





if __name__=="__main__":
	a=job_queue()
	a.add_task(1,100)
	a.add_task(0,1000)
	print a.get_nexttask()

	
	
