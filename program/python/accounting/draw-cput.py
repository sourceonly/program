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



cput_array=get_value_all("select sum(i_cput),start_time from pbs_breakdown_full group by start_time order by start_time")

time_axis=map(lambda x:x[1],cput_array);
cput=map(lambda x:x[0]/3600,cput_array);

save_data('cput_1h.csv',cput_array);


import matplotlib.pyplot as plt;
fig1,ax1  = plt.subplots();
ax1.plot(time_axis,cput);
ax1.grid(True);

plt.savefig("cput.eps",format='eps');

plt.show();

