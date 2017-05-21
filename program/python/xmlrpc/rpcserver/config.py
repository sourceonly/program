

class config:
	def __init__(self,configfile): 
		f=open(configfile,'r')
		self.dict={}
		for i in f:
                        if i.rstrip()=='':
                                continue
			(key,value)=i.rstrip().split('=',1)
			self.dict[key]=value
		f.close()
	def get_value(self,key): 
		if not self.dict.has_key(key):
			return 	
		return self.dict[key]
	def get_value_list(self,key):
		if not self.dict.has_key(key):
			return
		return self.dict[key].split(',')
			
		

