


import numpy as np
import psycopg2 as pg

conn=pg.connect("dbname=pbs_account user=source")
cur=conn.cursor();



def get_value_all(sq_ex):
    cur.execute(sq_ex);
    return cur.fetchall();
def get_value(sq_ex,col=0):
    cur.execute(sq_ex);
    return map(lambda x:x[col],cur.fetchall());

def save_data(filename,l) :
    f=open(filename,'w');
    for i in l:
        l1=i[0];
        l2=i[1];
        f.write("%s,%s" % (l1,l2,));
        f.write('\n')
    f.close();

queue_array=get_value_all("select ncpus_q, start_time from pbs_interval_full ORDER BY start_time")
run_array=get_value_all("select ncpus_r, start_time from pbs_interval_full ORDER BY start_time");


save_data("queue_cpu_vs_time.csv",queue_array);
save_data("run_cpu_vs_time.csv",run_array);



time_axis1=map(lambda x:x[1],queue_array);
queue_cpu=np.array(map(lambda x: x[0] if x[0] else 0 ,queue_array))
time_axis2=map(lambda x:x[1],run_array);
run_cpu  =np.array(map(lambda x: x[0] if x[0] else 0 ,run_array));



cur.close()
conn.close()

import matplotlib.pyplot as plt;
fig1,ax1  = plt.subplots();
ax1.plot(time_axis1,queue_cpu+run_cpu,'r');

ax1.plot(time_axis2,run_cpu,'b');
ax1.grid(True);

plt.savefig("run_cpu_vs.eps",format='eps');

plt.show();







