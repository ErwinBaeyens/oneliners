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

#
with open('../nodes.cfg', 'r') as nf:
    nodes = nf.read()

node_lines = nodes.splitlines()
node_data = list()

for line in node_lines:
    if line != "":
        if line.startswith('['):
           _line = '"host" : '+'"'+line[1:-1]+'"'
           node_data.append(_line)
           del _line
        else:
           line.replace("=",'" : "')
           line+='"'
           _line='"'+line
           node_data.append(_line)
           del _line

