update ports set service = 'marvinweb https' where port = 8443;
update ports set service = 'mona' where port = 9900;
update ports set service = 'mongodb' where port >= 270016 and port <= 270030;
update ports set service = 'nginx general'where port = 10080;
update ports set service = 'arakoon catchup' where port >= 29000 and port <= 29040;
update ports set service = 'arakoon catchup' where port >= 31010 and port <= 31050;
update ports set service = 'arakoon client' where port >= 20000 and port <= 20099;
update ports set service = 'arakoon client' where port >= 22010  and port <= 22099;
update ports set service = 'arakoon messaging' where port >= 24000 and port <= 24099;
update ports set service = 'arakoon messaging' where port >= 26010 and port <= 26099;
update ports set service = 'csbridge' where port = 9600 and port = 9609;
update ports set service = 'dssclientdaemon axm' where port >= 10000 and port <= 10009;
update ports set service = 'dssclientdaemon management' where port >= 11010 and port <= 11019;
update ports set service = 'dssclientdaemon s3' where port >= 11000 and port <= 11009;
update ports set service = 'dssrepairdaemon' where port >= 13000 and port <= 13099;
update ports set service = 'dssstoragedaemon' where port >= 12000 and port <= 12099;
update ports set service = 'haproxy' where port = 443 ;
update ports set service = 'identitybridge' where port >= 9300 and port <= 9309;
update ports set service = 'keyrouter' where port >= 9200 and port <= 9209;
update ports set service = 'samurai' where port >= 4001 and port <= 4005;
update ports set service = 'ui https' where port = 10443;
update ports set service = 'scalerd manager' where port >= 9700 and port <= 9709;
update ports set service = 'scalerdbmgr' where port >= 9500 and port <= 9509;
update ports set service = 'scalermgmt' where port >= 9400 and port <= 9409;
update ports set service = 'scalermgmt https' where port = 9443;
update ports set service = 'sparkexecutor messaging' where port >= 9810 and port <= 9814;
update ports set service = 'sparkexecutor ui' where port >= 9815 and port <= 9814;
update ports set service = 'sparkmaster manager' where port >= 9805 and port <= 9809;
update ports set service = 'sparkmaster messaging' where port >= 9800 and port <= 9804;
update ports set service = 'sparkmaster ui' where port >= 9795 and port <= 9799;
update ports set service = 'zookeepernode client' where port >= 28000 and port <= 28004;
update ports set service = 'zookeepernode election' where port >= 28010 and port <= 28014;
update ports set service = 'zookeepernode messaging' where port >= 28005 and port <= 28009;
update ports set service = 'elasticserachdb http' where port >= 8092 and port <= 8094;
update ports set service = 'elasticserachdb meta' where port >=  8095and port <= 8097;
