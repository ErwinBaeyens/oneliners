from marvin_lib.network import ha
import json

# get the guid of the column network
c_guid = cli.marvin.column.list()[0]['guid']

# query the column for the guids of the column nodes
c_nodes = json.loads(ha.get('/model/column/Column1/action/proxy/machine'))

for col in c_nodes['machine']:
    if col['status'] == 'NOTINITIALIZED':
        api_call = '/model/column/Column1/action/proxy/machine/%s/action/configure'%(col['guid'])
        tasks=json.loads(ha.post(api_call)
        while tasks['machine']['status'] == 'CONFIGURING':
        json.loads(ha.get('/model/column/Column1/action/proxy/machine/
