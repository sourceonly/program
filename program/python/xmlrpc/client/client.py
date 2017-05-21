import xmlrpclib

s = xmlrpclib.ServerProxy('http://psn001:8000')


#print s.pow(2,3)  # Returns 2**3 = 8
#print s.add(2,3)  # Returns 5
#print s.div(5,2)  # Returns 5//2 = 2

#print s.run_command1("/bin/bash ")[0]
#print xmlrpclib.dumps((5,2,),'div')

# Print list of available methods

#print s.test_args("abc",1,2,3);


#print s.do_submit("software=starccm\nncpus=2  NCPUS=2 cwd=/home/source","LMX_LICENSE_FILE=6200@px00 PATH=a.path")
#print s.do_submit("software=starccm STARCCM=abc NCPUS=2 cwd=/home/source  ","LMX_LICENSE_FILE=6200@px00 PATH=a.path")


#print s.do_submit("software=testapp\t NCPUS=2 ARGS= JOBNAME=test OUTPUT=a.log QUEUE=q_x86_expr COMMAND=/bin/env cwd=/GPFS/felemx/tmp","LMX_LICENSE_FILE=6200@px00 PATH=a.path");





#print s.system.listMethods()
print s.do_submit("software=starccm\t NCPUS=4 JOBNAME=test-star OUTPUT=result.txt QUEUE=q_x86_expr SIMFILE=pipe_10000.sim JAVAFILE=batch.java cwd=/GPFS/felemx/test/startest/bsub-test","LMX_LICENSE_FILE=1999@psn008");

