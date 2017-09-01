#!/usr/bin/python
import time
import subprocess
import functools

rc=subprocess.Popen("psql pbs_account -f ./scheme/initdb.sql",shell=True)
rc.wait();


import os
log_location="account"
from multiprocessing import Pool

for root,dir,file in os.walk(log_location):
    input=map(lambda x: os.path.join(root,x),file)
import re


from logtool.tools import *

from sqltools import *
from functools import partial
from multiprocessing import Pool
if __name__=="__main__":


	import psycopg2
	conn=psycopg2.connect("dbname=pbs_account user=source");
	cur=conn.cursor();
	
	def sql_ex_mul(x):
		return sql_ex(x,conn,cur)
	def file_op_mul(p):
		return file_op(p,sql_ex_mul);
	p=Pool(processes=1);	
	p.map(file_op_mul,input)
	cur.close()
	conn.close()
