import numpy;
import functools


import psycopg2
conn=psycopg2.connect("dbname=pbs_account user=source");
cur=conn.cursor();


cur.execute("select * from (select jobid, jstart,jend, (jend-jstart)*ncpus as v, ncpus from  (select jobid, cast(stime as bigint) as jstart, cast(etime as bigint) as jend , cast(ncpus as bigint ) as ncpus from pbs_task ) as p  ) as q where v>0;")

value=cur.fetchall()
cur.close()
conn.close();


#print value


import numpy as np
a=np.array(value)



start_time=np.array(map(int,a[:,1]))
end_time=np.array(map(int,a[:,2]))
cost=np.array(map(int,a[:,3]));
ncpus=np.array(map(int,a[:,4]));





time_max=max(max(start_time),max(end_time));
time_min=min(min(start_time),min(end_time));


time_slice=np.arange(time_min,time_max,3600*24*7);
def my_sub(x,y):
	return max(y-x,0);

res_array=[];
for i in time_slice:
	i_start=np.array(map(lambda x: my_sub(x,i)  ,start_time))
	i_end=np.array(map(lambda x: my_sub(x,i), end_time))
	res_array.append(np.dot(np.subtract(i_start,i_end),ncpus));
        print i_start,i_end;
#	pass

print  1

dv=[0]
for  i in range(len(res_array)-1):
	dv.append(res_array[i+1]-res_array[i])



from pylab import * 
figure(1)
plot(range(len(dv)),dv)
grid(True)

figure(2)
from matplotlib import pyplot as plt
plt.hist(dv[10:],bins=50);
grid(True)


figure(3)

plot(numpy.abs(numpy.fft.fft(dv-np.mean(dv))))
show();






