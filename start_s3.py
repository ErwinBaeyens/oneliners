import os
import sys
import time
import select
import logging
from argparse import ArgumentParser
import subprocess
from lib import daemon

from lib.utils import Resource


from longevity.modules.s3.s3 import S3_backend

system_bucket = 'system-f8c9dded-66f0-458d-850b-0f98782bd62b'

#
with open('../nodes.cfg', 'r') as nf:
    nodes = nf.read()

node_lines = nodes.splitlines()
node_data = {}


for line in node_lines:
    if line != '':
        if line.startswith('['):
            _line = {line[1:-1]:{}}
            node_data.update(_line)
            del(_line)
            host=line[1:-1]
        else:
            k, v = line.split('=')
            _line = {k.strip():v.strip()}
            node_data[host].update(_line)
            del (_line%cpaste)

con = S3_backend(node_data['scaler1']['ip'], 80, node_data['scaler1']['apikey'], node_data['scaler1']['secret'], https=False)


result = con.get_bucket_contents(system_bucket)
print result[0]
if result[1] == 'true':
    do_continuation()

