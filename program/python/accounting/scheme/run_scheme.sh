#!/bin/bash
cd $(dirname $0) ;
psql pbs_account -f jobs.sql
psql pbs_account -f cput_seq.sql

