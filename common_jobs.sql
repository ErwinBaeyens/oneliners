INSERT INTO longevity.common_jobs_list(job_type, description, parameters)
VALUES
	('s3', '16 MB PUT', '-a 4 -D 15 -r ''[["PUT", 1.0]]'' -R ''[[16777216, 1]]'' -n nodes.cfg'),
	('s3', '8mb 16mb PUT', '-a 2 -D 2 -r ''[["PUT", 1.0]]'' -R ''[[8388608, 0.5],[16777216, 0.5]]'' -c nodes.cfg'),
	('s3', 'add 1 MB', '-a 1 -D 1 -r ''[["PUT",1.0]]'' -R ''[[1048576, 1]]'' -n nodes.cfg'),
	('s3', '2GB job ', '-a 1 -D 1 -r ''[["PUT", 1.0]]'' -R ''[[2147483648, 1]]'' -n nodes.cfg -C 10485760'),
	('s3', '5 mixed bucket operations mostly GET', '-a 1 -D 5 -b -r ''[["PUT", 0.2], ["GET", 0.7], ["DEL", 0.1]]'' -R ''[[1, 1.0]]'' -n nodes.cfg'),
	('s3', '5 gb put', '-a 1 -D 1 -r ''[["PUT", 1.0]]'' -R ''[[5368709120, 1]]'' -n nodes.cfg -C 104857600');

