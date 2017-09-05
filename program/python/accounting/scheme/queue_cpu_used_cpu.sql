DROP TABLE pbs_run_cpu;		
select *
INTO pbs_run_cpu
from pbs_interval CROSS JOIN pbs_jobs where start_time > stime AND start_time < etime;


DROP TABLE pbs_queue_cpu;
select *
INTO pbs_queue_cpu
from pbs_interval CROSS JOIN pbs_jobs where start_time > ctime AND start_time < stime;





DROP TABLE pbs_interval_full;

select *
INTO
pbs_interval_full
FROM
(select sum(ncpus) as ncpus_r, start_time from pbs_run_cpu GROUP BY start_time) as r

RIGHT OUTER JOIN
(select  *
FROM
(select sum(ncpus) as ncpus_q, start_time from pbs_queue_cpu GROUP BY start_time) as q RIGHT OUTER JOIN pbs_interval USING (start_time) ) as p
USING (start_time) ORDER BY start_time;

