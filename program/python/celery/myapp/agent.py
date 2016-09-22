from __future__ import absolute_import
from myapp.celery import app
import socket
import sys
import subprocess;
import time
@app.task
def add(x,y):
    time.sleep(y%3);
    return {'the value is ':str(x+y),'node_name':socket.gethostname()}

@app.task
def writefile():
    out=open('/tmp/data.txt','w')
    out.write('hello'+'\n')
    out.close()

@app.task
def mul(x,y):
    return x*y

@app.task
def xsum(numbers):
    return sum(numbers)

@app.task
def getl(stri):
    return getlength(stri)


def getlength(stri):
    return len(stri)



@app.task
def safe_wt(fileno,content):
	try:
		f=open(fileno,"a+")
		f.write(content)
		f.close();
	except:
		pass
	return
@app.task
def runprocess(cmd='ls',out="outfile",err="errfile"):
	rc=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE);
	outc,errc=rc.communicate()
	safe_wt(out,outc)
	safe_wt(err,errc)	
	return out

