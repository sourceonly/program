/* init db from raw accounting input */ 

DROP TABLE pbs_task;
CREATE TABLE pbs_task (jobid VARCHAR(20),ctime VARCHAR(100),stime VARCHAR(100), etime VARCHAR(100), ncpus VARCHAR(100),puser VARCHAR(100),pgroup VARCHAR(100),platform VARCHAR(100),software VARCHAR(100));


