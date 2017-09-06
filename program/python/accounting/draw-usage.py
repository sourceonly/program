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



m_array=get_value_all("select avg(c_usage), date_trunc('month',start_time) as m from pbs_usage group by m order by m;")

time_axis_m=map(lambda x:x[1],m_array);
usage_m=map(lambda x:x[0],m_array);

save_data('cpu_usage_vs_month.csv',m_array);

d_array=get_value_all("select avg(c_usage), date_trunc('day',start_time) as d from pbs_usage group by d order by d;")

time_axis_d=map(lambda x:x[1],d_array);
usage_d=map(lambda x:x[0],d_array);

save_data('cpu_usage_vs_day.csv',d_array);

dow_array=get_value_all("select avg(c_usage), EXTRACT('dow' from start_time) as dow from pbs_usage group by dow order by dow;")

time_axis_dow=map(lambda x:x[1],dow_array);
usage_dow=map(lambda x:x[0],dow_array);

save_data('cpu_usage_vs_dow.csv',d_array);



cur.close();
conn.close();

import matplotlib.pyplot as plt;
fig1,ax1  = plt.subplots();
ax1.plot(time_axis_m,usage_m);
ax1.grid(True);

plt.savefig("cpu_usage_vs_month.eps",format='eps');


fig2,ax2  = plt.subplots();
ax2.plot(time_axis_d,usage_d);
ax2.grid(True);
plt.savefig("cpu_usage_vs_day.eps",format='eps');

fig3,ax3  = plt.subplots();
ax3.plot(time_axis_dow,usage_dow);
ax3.grid(True);
plt.savefig("cpu_usage_vs_dow.eps",format='eps');



plt.show();

