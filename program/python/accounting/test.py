import psycopg2
import re
import functools

import multiprocessing

class sqltools():
    
    def __init__ (self,connect_info,lock=None):
        self.connect_info=connect_info;
        self.conn=None
        self.cur=None
        self.uchar=re.compile("[^A-za-z]");
        self.lock=lock;
    def make_cur(self):
        self.conn=psycopg2.connect(self.connect_info);
        self.cur=self.conn.cursor();
    def get_conn(self):
        return self.conn
    def get_cur(self):
        return self.cur;
    def close(self):
        conn=self.conn
        cur=self.cur
        
        self.conn=None
        self.cur=None
        
        conn.commit();
        cur.close();
        conn.close();
        
    def aclock(self):
        if self.lock:
            self.lock.acquire()
    def relock(self):
        if self.lock:
            self.lock.release()
    def make_event(self,time,r_type,jobid,infobody):
        self.cur.execute("INSERT INTO pbs_event (time,r_type,jobid) VALUES (%s,%s,%s)",(time,r_type,jobid,))
        self.update_job(time,jobid,infobody);
        self.conn.commit()
        
    def make_job(self,jobid,time):
        cur=self.cur
        cur.execute("select * from pbs_job_attr where jobid=\'"+jobid +"';");
        if cur.fetchone() == None :
            cur.execute("INSERT INTO pbs_job_attr (jobid,time) VALUES (%s,%s)",(jobid,time,));

    def make_res(self,res):
        cur=self.cur
        cur.execute("select * from pbs_resource where pbs_resource=\'"+ res +"';");
        if cur.fetchone() == None :
            self.aclock()
            cur.execute("INSERT INTO pbs_resource (pbs_resource) VALUES (%s)",(res,));
            cur.execute("ALTER TABLE pbs_job_attr ADD COLUMN res_" + res + " VARCHAR(10000)")
            self.relock()
            
    def res_trans(self,res):
        return self.uchar.sub("_",res)
    def update_job(self,time,jobid,infobody):
        
        self.make_job(jobid,time);
        cur=self.cur
        
        cur.execute("select * from pbs_job_attr where time > cast ('"+ time + "'as timestamp) and jobid='"+jobid+"';" )
        
        import time
        if cur.fetchall() != []:
            return 
        info_pair=body_string(infobody);

        if not info_pair:
            return 
        for i in info_pair:
            
            key=i[0]
            key=self.res_trans(key)

            if len(i)<2:
                continue
            value=i[1];
            self.make_res(key);
            self.aclock()
            cur.execute("UPDATE pbs_job_attr set res_" + key + "='"+value+ "' where jobid='" + jobid+"'");
            self.relock()

        
def line_parse(line_content):
    line=line_content.strip('\n');
    line_list=line.split(';');
    if line_list[1]!='E' :
        return '';
    pair={};
    for i in line_list[3].split(' '):
        if i.find('=')<0:
            continue;
        key,value=i.split('=',1);
        pair[key]=value;
    ret=[];
    ret.append(line_list[0]);
    ret.append(line_list[1]);
    ret.append(line_list[2]);
    ret.append(pair);
    return ret;

            

def sql_ex(string,conn,cur):
    line_list=line_parse(string);
    if line_list=='':
        return
    if len(line_list)<4:
        return;
    print line_list
    jobid=line_list[2];
    start_t=line_list[3]['start'];
    end_t=line_list[3]['end'];
    ncpus=line_list[3]['Resource_List.ncpus'];
    cur.execute("INSERT INTO  pbs_task (jobid,stime,etime,ncpus) VALUES (%s,%s,%s,%s)",(jobid,start_t,end_t,ncpus));
    conn.commit();

def body_string(string):
    if string.find('=') < 0 :
        return
    body_list=re.split(" +",string);
    return map(lambda x:x.split('='),body_list);




f=open('account/20170531','r')
for i in f:
    print i;
    line_parse(i);


