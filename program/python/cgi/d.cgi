#!/usr/bin/python

print "Content-type: text/html"
print ""

import sys
#print sys.stdin.read()
import cgi
form=cgi.FieldStorage()

#for i in form: 
#	print  i;
#	print form.getvalue(i)


content=form.getvalue('filename')
f=open("/tmp/test",'wb')
f.write(content)
f.close()
