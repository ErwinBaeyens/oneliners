SELECT
     ports.ip as address,
     hosts.hostname AS hostname,
     ports.port,
     ports.service  
FROM ports join hosts on
     ports.ip = hosts.ip 
WHERE
     hosts.ip NOT LIKE '%.1' AND 
     hosts.ip NOT LIKE '%.2' AND 
     hosts.ip NOT LIKE '%.3'
ORDER BY
     hostname,
     address,
     port
