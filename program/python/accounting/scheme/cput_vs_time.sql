select start_time,sum(i_cput) from pbs_breakdown_full group by start_time order by start_time;


select start_time,sum(i_cput) from pbs_breakdown_full  where pgroup='CFD' group by start_time order by start_time;

select start_time,sum(i_cput) from pbs_breakdown_full  where software='Optistruct' group by start_time order by start_time;


select start_time,sum(i_cput) from pbs_breakdown_full  where puser='yanzichao' group by start_time order by start_time;
