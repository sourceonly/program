import socket
import subprocess
class pynode:
	def __init__(self): 
		self.snap={}
		self.host=socket.gethostname()
		self.snap={'total_cpus':'4'}
		self.snap['used_cpus']=2
		f=open('config','r')
		for i in f: 
			if	i.find('=') >=0 : 
				k,v=i.strip('\n').split('=',1)
				self.snap[k]=v
		f.close()
		self.tasks={}
		
	def report(self):
		return self.snap

	def format_report(self):
		dict=self.report()
		print self.host,":"
		for i in dict: 
			print "\t%10s = %20s" % (i,dict[i]) 

	def add_tasks(self,cmd,outputfile): 
		f=open(outputfile,'w')	
		rc=subprocess.Popen(cmd,shell=True,stdout=f)
		self.tasks[rc]={}
		self.tasks[rc]['fd']=f
		return rc
	def update(self): 
		tasks_to_clean=[]
		for i in self.tasks:
			if i.poll()!=None:
				tasks_to_clean.append(i)
		for i  in tasks_to_clean:
			self.tasks.pop(i)
		
	def remove_tasks(self,p):
		dict=self.tasks.pop(p)
		p.terminate();
		dict['fd'].close()
		
			
	
	
if __name__ =="__main__": 
	a=pynode()
	a.format_report()
	
