select 
	*
from s3_object_history
Where
	ts_executed between '2016-06-10 00:00:00'::timestamp
		        and '2016-07-19 00:00:00'::timestamp;
			
