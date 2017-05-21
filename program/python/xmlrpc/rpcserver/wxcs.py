import subprocess
import config
import sys
import re
import os
import tempfile

class wxcs () : 
    def __init__ (self,file="config") :
	self.file=file
        self.conf=config.config(file);
        pass
    def run_command1(self,string):
        rc=subprocess.Popen(string,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE);
        return rc.communicate();
    
    def run_command2(self,args):
        pass
    
    def sanity_check(self,data): 
        if not data.has_key("software"):
            return "ERROR: you must specify a software"
        if not data.has_key("NCPUS"):
            return "ERROR you must specify NCPUS"
        
        return "";

    def make_dict(self,string):
        dict={};
        for i in re.split("\s+",string):
            if i=='': 
                continue
            if i.find("=") < 0 :
                dict[i]=None;
                continue;
            k,v=i.split("=",1);
            dict[k]=v;
        return dict;

    def do_submit(self,submit_data, submit_env) :

        ''' dispatcher for doing submit '''
	self.conf=config.config(self.file);
        data=self.make_dict(submit_data);
        env=self.make_dict(submit_env);
        err_message=self.sanity_check(data);
        message='';
        
        if not err_message=='': 
            return '',err_message;

        content,err=self.make_submit(data,env);
        if not err=='':
            return '',err;
        
        script_file=self.make_script(content);
        
        out,err=self.submit_script(script_file,data);
        if not err=='':
            return '',err;
        
        message+=out
        err_message+=err

        
        return message,err_message;
    def make_mpifile(self,dict) :
        dict['MPI_FILE']='./machine'
        content=''
        content+="echo files > ./machinefile\n"
        return content,''
    
    def make_resub(self,dict,content) :
        for i in dict:
            pattern=re.compile("@%s@"%(i,));
            content=pattern.sub(dict[i],content);
            
        remain=re.compile("@([^@]*)@");
        if remain.search(content):
            return content,"error: %s is not provide" % (remain.search(content).group(1),);
        return content,'';
    
        
    def submit_script(self,script_file,data):
	os.chmod(script_file,0700);
        bsub='bsub -J @JOBNAME@ -o @OUTPUT@ -q @QUEUE@ -n @NCPUS@ -appplugin %s' % (script_file,);
        if data.has_key('cwd'):
            workdir=data['cwd'];
        else:
            workdir=None;
        bsub=self.make_resub(data,bsub);
        rc=subprocess.Popen(bsub,shell=True,cwd=workdir,stdout=subprocess.PIPE,stderr=subprocess.PIPE);
        out,err=rc.communicate();
        return out,err;
        
    def make_script(self,content):
	tmpdir=self.conf.get_value("tmpdir");
        o,file=tempfile.mkstemp("submit","file",tmpdir);
        f=open(file,"w");
        f.write(content);
        f.write('\n');
        f.close();
        return file;
    def test_args(self,*args):
        ''' test for unknown numbers args ''' 
        a=""
        for i in args:
            a+=repr(i);
            a+='\n';
        return a

    def make_header(self,env):
        content="#!/bin/bash\n"
        for i in env:
            content+="export %s=\"%s:$%s\"\n"% (i,env[i],i,)          ;
        return content,'';
    def make_body(self,data):
        soft=self.conf.get_value(data['software']);
        return self.make_resub(data,soft);


    def make_submit(self,data,env):
        content,err=self.make_header(env);
        c,e=self.make_mpifile(data);
        content+=c;
        err+=e;
        
        c,e=self.make_body(data);
        content+=c;
        err+=e;
        
        return content,err;
        

if __name__=="__main__":
    a=wxcs();
    print a.do_submit("software=testapp\t NCPUS=2 ARGS= JOBNAME=test OUTPUT=a.log QUEUE=q_x86_expr COMMAND=/bin/env cwd=/GPFS/felemx/tmp","LMX_LICENSE_FILE=6200@px00 PATH=a.path");
