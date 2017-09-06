#!/bin/bash
cd $(dirname $0) ;
psql pbs_account -f jobs.sql
psql pbs_account -f level.sql
psql pbs_account -f cput_seq.sql
psql pbs_account -f queue_cpu_used_cpu.sql

