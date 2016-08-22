#!/usr/bin/env python

import os
import sys

hosts = { '172.16.1.1':'HGST-S3-DC01-R01-SG01',
          '172.16.1.11':'HGST-S3-DC01-R01-SE01',
          '172.16.1.12':'HGST-S3-DC01-R01-SE02',
          '172.16.1.13':'HGST-S3-DC01-R01-SE03',
          '172.16.1.14':'HGST-S3-DC01-R01-SE04',
          '172.16.1.15':'HGST-S3-DC01-R01-SE05',
          '172.16.1.16':'HGST-S3-DC01-R01-SE06',
          '172.17.1.1':'HGST-S3-DC02-R01-SG01',
          '172.17.1.11':'HGST-S3-DC02-R01-SE01',
          '172.17.1.12':'HGST-S3-DC02-R01-SE02',
          '172.17.1.13':'HGST-S3-DC02-R01-SE03',
          '172.17.1.14':'HGST-S3-DC02-R01-SE04',
          '172.17.1.15':'HGST-S3-DC02-R01-SE05',
          '172.17.1.16':'HGST-S3-DC02-R01-SE06',
          '172.18.1.1':'HGST-S3-DC03-R01-SG01',
          '172.18.1.11':'HGST-S3-DC03-R01-SE01',
          '172.18.1.12':'HGST-S3-DC03-R01-SE02',
          '172.18.1.13':'HGST-S3-DC03-R01-SE03',
          '172.18.1.14':'HGST-S3-DC03-R01-SE04',
          '172.18.1.15':'HGST-S3-DC03-R01-SE05',
          '172.18.1.16':'HGST-S3-DC03-R01-SE06'}

for i in [16, 17, 18]:
    for j in [1, 11, 12, 13, 14, 15, 16]:
        ip = "172.%d.1.%d"%(i, j)
        if not os.path.isdir(hosts[ip]):
            try:
                os.mkdir(hosts[ip])
            except OSError:
                print "could not create dir: %s.  please check." % (hosts[ip])
                sys.exit(1)
        # cd to dir
        # rsync remote dir in current dir
        # return from dir
        # make tar

        os.chdir(hosts[ip])
        cmdline = "rsync -avz marvin@%s:/opt/ampli/var/log/marvinweb/ marvinweb"% (ip)  
        os.system(cmdline)
        os.chdir("..")
        cmdline2 = "tar cvf %s.tar %s/*" % (hosts[ip], hosts[ip])
        os.system(cmdline2)
        
