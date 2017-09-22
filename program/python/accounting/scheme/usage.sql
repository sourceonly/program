s
DROP TABLE pbs_usage;





select cput/m_cpu/3600*100 as c_usage, start_time
INTO pbs_usage
from 
(select sum(i_cput) as cput,start_time,avg(max_cpu) as m_cpu from pbs_breakdown_full GROUP BY start_time) as a;

-- get day usage
-- select avg(c_usage), date_trunc('day',start_time) as d from pbs_usage group by d order by d;


-- get month usage
-- select avg(c_usage), date_trunc('month',start_time) as m from pbs_usage group by m order by m;

-- get day of week usage
-- select avg(c_usage), EXTRACT('dow' from start_time) as dow from pbs_usage group by dow order by dow;


-- get work hour usage
-- select avg(c_usage) from (select c_usage, EXTRACT('isodow' from  start_time) as iso_dow, start_time, date_trunc('day',start_time) as d from pbs_usage) as a where iso_dow < 6 AND start_time > d + interval '8 hour' AND start_time < d + interval '8 hour' + interval '10 hour';


-- get non-work hour usage
-- select avg(c_usage) from (select c_usage, EXTRACT('isodow' from  start_time) as iso_dow, start_time, date_trunc('day',start_time) as d from pbs_usage) as a where (iso_dow < 6 AND start_time < d + interval '8 hour' OR start_time > d + interval '8 hour' + interval '10 hour') OR iso_dow>5;




