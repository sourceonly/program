
import json
class json_message():
	def __init__(self): 
		pass
	def encode(self,header,obj):
		if not obj: 
			return
		dict={}	
		dict['header']=header
		dict['body']=obj
		return json.dumps(dict)
	def decode(self,jstring): 
		if not jstring: 
			return None
		return json.loads(jstring)
	def get_key(self,key, jstring):
		if not jstring :
			return None
		try:
			return self.decode(jstring)[key]
		except: 
			return 
	def get_header(self,jstring):
		return self.get_key('header',jstring) 
	def get_body(self,jstring):
		return self.get_key('body',jstring)
	
