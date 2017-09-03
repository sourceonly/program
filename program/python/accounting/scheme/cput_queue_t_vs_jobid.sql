select
jobid,
cpu*(epoch_etime-epoch_stime) as cput,
(epoch_stime-epoch_ctime) as queuet
INTO pbs_cput
from
(select jobid as jobid,
cast(ctime as bigint) as epoch_ctime,
cast(etime as bigint) as epoch_etime,	
cast(stime as bigint) as epoch_stime,	
to_timestamp(cast(ctime as double precision)) as c_time,
to_timestamp(cast(stime as double precision)) as s_time,
to_timestamp(cast(etime as double precision)) as e_time,
cast(ncpus as bigint) as cpu
from pbs_task ) as tmptable;







