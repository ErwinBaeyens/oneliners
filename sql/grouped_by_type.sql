Select
	s3_object_history.s3_type,
	count(s3_object_history.id),
	s3_object_history.object_size_mb,
	sum(s3_object_history.object_size_mb)
FROM s3_object_history
WHERE ts_executed BETWEEN '2016-06-10 00:00:00'::timestamp
      		  AND  	  '2016-07-19 00:00:00'::timestamp
group BY s3_type, object_size_mb
order by object_size_mb;