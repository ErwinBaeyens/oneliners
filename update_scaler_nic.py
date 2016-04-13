from marvin_lib import ha
import json
import time


# setup the new network data

networkdc = {}
networkdc['network'] = '<network address>'
networkdc['netmask'] = '<network netmask>'
networkdc['status'] = 'ENABLED'
networkdc['name'] = 'PublicLanDC'


# create the new network

print ha.post('/model/network', data=json.dumps(networkdc))


# get the guid from the new network

networks = json.loads(ha.get('/model/network'))
for net in networks['network']:
    if net['name'] ==  networkdc['name']:
        net_guid = net['guid']


# get machine data and get nic data

for machine in cli.marvin.machine.list():
    print machine['name']
    for nic in machine['nic']:
        print nic['device'], nic['guid'], nic['address']

        
# modify the nicUpdate object

nicUpdate = {}
nicUpdate['address'] = '<new ip address>'
nicUpdate['netmask'] = '<new netmask>'
nicUpdate['network'] = net_guid


# push the new data

print ha.put('/model/machine/<host name>/nic/<nic_guid>', data = json.dumps(nicUpdate))


# reconfigure the host

task = cli.marvin.machine.configure('<hostname>')


# wait for the reconfiguration task to finish

id = task['guid']
while True:
    task = cli.marvin.task.get(id)
    if task['finished'] == True:
        time.sleep(5)
        print 'waiting'
    else:
        break

    
# verifiy

for machine in cli.marvin.machine.list():
    print machine['name']
    for nic in machine['nic']:
        print nic['device'], nic['guid'], nic['address']
