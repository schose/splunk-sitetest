### Test Results

- all tests were made with Splunk Enterprise v8
- 6500 Buckets with 27G size were mountet to default index (main) and wait until replication was done
- data have to been copied 3x - 1h of testing is 27GB x 3 / 3600 seconds = 23MB/s
- EC2 instances were m5.2xlarge(8vCPU, 32GB RAM)

| scenario | test_start | test_end | time taken (minutes)| sf/rf| comment | 
|----------|------------|----------|---------------------|------|---------|
|1site-8instances-sf4 |12/08/2019 10:41:00 | 12/08/2019 11:36:00 | 55.00 | | comment |
|2site-8instances-sf4 | 12/08/2019 17:00:00 |12/08/2019 18:00:00 | 60.00 |site_replication_factor = origin:2,site1:2,site2:2,total:4 site_search_factor = origin:2,site1:2,site2:2,total:4| [timeline](pics/2site-8instances-sf4-1.png) |
|2site-8instances-sf4 | 12/08/2019 21:25:00	| 12/08/2019 22:30:00	| 65.00 | site_replication_factor = origin:2,site1:2,site2:2,total:4 site_search_factor = origin:2,site1:2,site2:2,total:4| [timeline](pics/2site-8instances-sf4-2.png) [buckets](pics/2site-8instances-sf4-2-buckets.png)|
|2site-8instances-sf4 | 12/08/2019 21:25:00	| 12/08/2019 22:30:00	| 65.00 | site_replication_factor = origin:2,site1:2,site2:2,total:4 site_search_factor = origin:2,site1:2,site2:2,total:4| [timeline](pics/2site-8instances-sf4-3.png) [buckets](pics/2site-8instances-sf4-3-buckets.png)|
|4site-8instances-sf4 | 12/08/2019 19:25:00*	| 	12/08/2019 22:35:00*	| 190.00* - giving up* | site_replication_factor = origin:1,site1:1,site2:1,site3:1,site4:1,total:4 site_search_factor = origin:1,site1:1,site2:1,site3:1,site4:1,total:4| [timeline](pics/4site-8instances-sf4-1.png) [buckets](pics/4site-8instances-sf4-1-buckets.png)[indexes](pics/4site-8instances-sf4-1-indexes.png)|
|4site-12instances-sf4 | 12/08/2019 20:20:00* |	12/08/2019 22:45:00*	 | 145.00*	 | site_replication_factor = origin:1,site1:1,site2:1,site3:1,site4:1,total:4 site_search_factor = origin:1,site1:1,site2:1,site3:1,site4:1,total:4| [timeline](pics/4site-8instances-sf4-1.png) [buckets](pics/4site-8instances-sf4-1-buckets.png) [indexes](pics/4site-8instances-sf4-1-indexes.png)|
|4site-12instances-sf4 | 12/08/2019 20:20:00* |	12/08/2019 22:45:00*	 | 145.00*	 | site_replication_factor = origin:1,site1:1,site2:1,site3:1,site4:1,total:4 site_search_factor = origin:1,site1:1,site2:1,site3:1,site4:1,total:4| [timeline](pics/4site-8instances-sf4-2.png) [buckets](pics/4site-8instances-sf4-2-buckets.png) [indexes](pics/4site-8instances-sf4-2-indexes.png)|


- * giving up