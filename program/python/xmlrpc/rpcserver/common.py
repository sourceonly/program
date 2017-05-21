import subprocess
import config
import sys
import re

class commonCommand () : 
    def __init__ (self,file="config") :
        self.conf=config.config(file);
        pass
    def run_command1(self,string):
        rc=subprocess.Popen(string,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE);
        return rc.communicate();
    
    def run_command2(self,args):
        pass
    
    def sanity_check(self,data): 
        if not data.has_key("software"):
            print >> sys.stderr , "you must specify a software"
            sys.exit(-1);
        if not data.has_key("ncpus"):
            print >> sys.stderr , "you must specify ncpus"
            sys.exit(-1);
        
    def make_dict(self,string):
        dict={};
        for i in re.split("\s+",string):
            if i.find("=") < 0 :
                dict[i]=None;
                continue;
            k,v=i.split("=",1);
            dict[k]=v;
        return dict;
    def submit(self,submit_data, submit_env) :
        data=self.make_dict(submit_data);
        env=self.make_dict(submit_env);
        self.sanity_check(data);
    
        return "abc"
    def test_args(self,*args):
        a=""
        for i in args:
            a+=repr(i);
            a+='\n';
        return a
        

if __name__=="__main__":
    a=commonCommand();
    a.submit("\nncpus=2 file","");
    
