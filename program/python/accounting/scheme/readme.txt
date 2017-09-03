run scheme order:

1. initdb.sql to init
2. read the accounting files ( by python )
3. jobs.sql to format all field to its type
4. level to get level information of every jobs (may be JOIN to the pbs_jobs? )
5. cput_queue_t_vs_jobid.sql ( jobs' cputime and queue time information)
6. cput_seq.sql to breakdown jobs into specific time intervals


