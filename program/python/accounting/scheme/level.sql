DROP TABLE pbs_job_result;
select *
INTO
pbs_job_result
from
(select
	jobid,
	CASE WHEN EXTRACT('dow' from morning)=0 THEN 4   /* if finish on Sun, then level to 4 */ 
	     WHEN EXTRACT('dow' from morning)=6 THEN 4   /* if finish on Sat, then level to 4 */ 
	     WHEN e_time < twilight AND c_time > morning THEN 1   /* workhour submit, workhour get result */
	     WHEN e_time > twilight AND c_time > morning THEN 2   /* workhour submit, after workhour  get result */


	     WHEN e_time < twilight AND c_time > (morning - interval '1 day') THEN 2   /* yesteday submit, workhour  get result */
	     WHEN e_time > twilight AND c_time > (morning - interval '1 day') THEN 3   /* yesteday submit, workhour  get result */
	     
	     WHEN e_time < twilight AND c_time > (morning - interval '2 day') THEN 3
	     WHEN e_time > twilight AND c_time > (morning - interval '2 day') THEN 3
	     /* the day before yesteday submit, workhour  get result */
	END as level
from
(select 
       (finish_day+interval '8 hour') as morning,             /* 8:00  start work */
       (finish_day+interval '8 hour' + interval '9 hour') as twilight,  /* 17:00  end work */ 
       jobid,
       c_time,
       e_time
from (select
jobid,
date_trunc('day',s_time) as finish_day,
cpu*(epoch_etime-epoch_stime) as cput,
(epoch_stime-epoch_ctime) as queuet,
c_time,
s_time,
e_time
from
(select jobid as jobid,
cast(ctime as bigint) as epoch_ctime,
cast(etime as bigint) as epoch_etime,	
cast(stime as bigint) as epoch_stime,	
to_timestamp(cast(ctime as double precision)) as c_time,
to_timestamp(cast(stime as double precision)) as s_time,
to_timestamp(cast(etime as double precision)) as e_time,
cast(ncpus as bigint) as cpu
from pbs_task) as tmptable) as tmptable2 ) as tmptable3 ) as tmptable4 INNER JOIN pbs_jobs USING (jobid) ORDER BY jobid;

