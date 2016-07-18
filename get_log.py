import json
import time

import subprocess

systembucket = "s3://system-ad5db554-854f-4252-a928-67112ed59c74"
cmd = []
cmd.append('s3cmd ls {}/machines/'.format(systembucket))
result = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out=err=None
out, err = result.communicate()
outl = out.splitlines()

machines=[]
for i in outl:
    machines.append(i.split()[1][-74:-1].split("_"))




def list_all_logs():
    pass

def parse_epoch():
    pass

def 
