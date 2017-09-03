DROP TABLE pbs_interval;

select start_time,
       end_time,
       EXTRACT('epoch' from start_time) as is_epoch,
       EXTRACT('epoch' from end_time) as ie_epoch
       INTO pbs_interval
       FROM
(select start_time,
       start_time + interval '1 hour' as end_time
FROM
(select generate_series(
       '2017-01-01'::date,
       '2017-07-01'::date,
       '1 hour'::interval) as start_time) as tmptable) as tmptable2;


DROP TABLE pbs_breakdown; 

select * 
	INTO pbs_breakdown
	FROM 
	pbs_interval as i
	CROSS JOIN
	pbs_jobs as j
	where
		(i.start_time, i.end_time) OVERLAPS (j.stime,j.etime);






