
from myapp.agent import add
from myapp.agent import runprocess


#for i in range(1000):
#	res=add.apply_async(args=[1,i],queue='machine1',routing_key='machine1')


#for i in range(10):
#	runprocess.apply_async(args=["dir","D:\\output","D:\\err"],queue='machine2',routing_key='machine2')
	


import sys
if __name__=="__main__":
	k=sys.argv[1]
	output=sys.argv[2]
	errput=sys.argv[3]
	cmd=" ".join(sys.argv[4:])
	res=runprocess.apply_async(args=[cmd,output,errput],queue=k,routing_key=k,id='hypermesh')
	


