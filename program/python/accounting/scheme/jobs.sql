/* scheme to run raw job info to its date types 
   epoch -- > int second 
   time  -- > timestamp 
   ncpus --> int 
   other --> strings 
*/
DROP TABLE pbs_jobs;
SELECT jobid,

       cast(ctime as bigint) as c_epoch,
       to_timestamp(cast(ctime as double precision)) as ctime,

       cast(stime as bigint) as s_epoch,
       to_timestamp(cast(stime as double precision)) as stime,
       
       cast(etime as bigint) as e_epoch,
       to_timestamp(cast(etime as double precision)) as etime,

       cast(ncpus as bigint) as ncpus,
       puser,
       pgroup,
       platform,
       software
       INTO
       pbs_jobs
       FROM pbs_task;
       
       		  
       
       
       
       
