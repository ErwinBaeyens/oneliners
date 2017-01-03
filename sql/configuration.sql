COPY configuration (id, module, key, value, value_type) FROM stdin;
1       \N      loglevel        10      int
2       \N      tick_duration   3600    int
3       Longevity       old_jobs        run     string
4       Longevity       start_job_list  1       int
5       Longevity       pidfile longevity.pid   string
7       S3      logfile logs/s3.log     string
10      ShardStat       logfile logs/shardstat.log      string
8       ShardedArakoon  logfile logs/shardedarakoon.log string
9       SARealityCheck  logfile logs/sarealitycheck.log string
6       Longevity       logfile logs/longevity.log      string
11      Database        email   <pdl-longevity_as5@sharedspace.onmicrosoft.com> string
\.

