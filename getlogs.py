import subprocess
import time
import calendar
import json

systembucket = "s3://system-ad5db554-854f-4252-a928-67112ed59c74"
deployment_id = 'ad5db554-854f-4252-a928-67112ed59c74'
column_deployment_id = '677a7d56-fd5e-473f-a415-5108f4ab002f'

col1 = 'fb327353-34bd-49e7-b5e5-c04d0640f138'
col2 = 'ef460bd4-8f8d-4fc8-a525-aafdf85654aa'
col3 = '089476a1-67d0-4cb6-9807-fd96ca78ebed'
col4 = '346903b2-bfc0-4033-b273-d1e7bb7e934c'
col5 = 'cc5cd825-5330-4a31-9d08-40f585c9bd9'
col6 = '25b8fb33-84e0-4bcb-a6d0-9f3771bba23'

scaler1 = 'ce7cab9a-a29e-4ab5-bc71-be9b02122aab'
scaler2 = '817a4113-947b-4342-abee-o3b3a506c45e5'
scaler3 = 'f6c81e00-2fc4-428b-8c63-2ca8574807d3'

path = "logs/opt/ampli/var/log/mongo"

cmd='s3cmd'
arg="ls"
argstr="".join(systembucket)
argstr2="/".join([deployment_id, scaler1, path, "*"])
time_val1 = time.mktime((2016,6,28,0,0,0,1,180,-1))
time_val2 = time.mktime((2016,6,29,0,0,0,1,180,-1))

subprocess.Popen()
