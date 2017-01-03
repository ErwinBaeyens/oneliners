SELECT 
	a.id,
	a.ts,  
	a.total_mb - b.total_mb AS size_diff,
	a.number_objects - b.number_objects AS amount_diff
 FROM 
	data_usage a 
 LEFT JOIN 
	data_usage b
 ON 
	a.id = b.id+1 
WHERE size_diff > 0;

