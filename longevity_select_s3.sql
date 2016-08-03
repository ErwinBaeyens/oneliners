/*****************************************************
 * Select all records from the database conserning  *
 * S3 actions for all versions                       *
 *                                                   *
 *****************************************************/ 

select 
	longevity.job.job_type, 
	longevity.job.ts_start,
	longevity.job.ts_end, 
	longevity.product_test_version.tag 
from longevity.job 
left outer join longevity.product_test_version
on
	longevity.job.product_version = longevity.product_test_version.id
where 
	longevity.job.product_version >= 2 AND
	longevity.job.product_version <= 4 AND
	longevity.job.job_type LIKE 's3%'
ORDER BY longevity.job.ts_start;

