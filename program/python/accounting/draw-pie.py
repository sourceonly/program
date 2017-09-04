import numpy as np
import psycopg2 as pg

conn=pg.connect("dbname=pbs_account user=source")
cur=conn.cursor();

def save_data(filename,l) :
    f=open(filename,'w');
    for i in l:
        l1=i[0];
        l2=i[1];
        f.write("%s,%s" % (l1,l2,));
        f.write('\n')
    f.close();
        

def get_value(sq_ex,col=0):
    cur.execute(sq_ex);
    return map(lambda x:x[col],cur.fetchall());

total_task = get_value("select count(*) from pbs_jobs");
total_use_cput = get_value("select sum(cput) from pbs_jobs");
software_list=get_value("select DISTINCT software from pbs_jobs");

software_count={};
software_cput={};



for i in software_list:
    software_count[i]=get_value("select count(jobid) from pbs_jobs where software='%s'" % (i))[0];
    software_cput[i]=get_value("select sum(cput) from pbs_jobs where software='%s'" % (i))[0];


group_count={};
group_cput={};

group_list=get_value("select DISTINCT pgroup from pbs_jobs");
for i in group_list:
    group_count[i]=get_value("select count(jobid) from pbs_jobs where pgroup='%s'" % (i))[0];
    group_cput[i]=get_value("select sum(cput) from pbs_jobs where pgroup='%s'" % (i))[0];
    

cur.close();
conn.close();


def sort_dict(dict) :
    p=[];
    for i in dict:
        p.append([i,dict[i]]);
    p.sort(key=lambda x:x[1]);
    return p;
    
    



from pylab import *
import matplotlib.pyplot as plt


# figure 1
# software cput pie 

cput_p=sort_dict(software_cput);
save_data('pie1.csv',cput_p);


labels = map(lambda x:x[0],cput_p);
sizes=map(lambda x:x[1],cput_p);
explode=map(lambda x:0,cput_p);

#explode = (0, , 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')


fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


plt.savefig("pie1.eps",format='eps');


# figure 2
# software no. of task pie;

soft_count_p=sort_dict(software_count);
save_data('pie2.csv',soft_count_p);


labels = map(lambda x:x[0],soft_count_p);
sizes=map(lambda x:x[1],soft_count_p);
explode=map(lambda x:0,soft_count_p);

fig2,ax2  = plt.subplots();

ax2.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig("pie2.eps",format='eps');




# figure 3
# group no. of task pie 


group_count_p=sort_dict(group_count);
save_data('pie3.csv',group_count_p);


labels = map(lambda x:x[0],group_count_p);
sizes=map(lambda x:x[1],group_count_p);
explode=map(lambda x:0,group_count_p);

fig3,ax3  = plt.subplots();

ax3.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig("pie3.eps",format='eps');




# figure 4  group pie of cputime

group_cput_p=sort_dict(group_cput);

save_data('pie4.csv',group_cput_p);


labels = map(lambda x:x[0],group_cput_p);
sizes=map(lambda x:x[1],group_cput_p);
explode=map(lambda x:0,group_cput_p);

fig4,ax4  = plt.subplots();

ax4.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.



plt.savefig("pie4.eps",format='eps');
plt.show()





