from marvin_lib.network import ha
import json
import time
import pprint

# setup the new network data

networkdc = {}
networkdc['network'] = '10.108.56.0'
networkdc['netmask'] = '255.255.254.0'
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
devices = {}

for machine in cli.marvin.machine.list():
    name = machine['name']
    for nic in machine['nic']:
        if nic['device'] == 'eth4':
            devices[name] = { 'eth':nic['device'],
                                'nic_guid':nic['guid']
            }



# modify the nicUpdate object
addresses = {}            
addresses['HGST-S3-DC01-R01-SG01']='10.108.56.222'
addresses['HGST-S3-DC02-R01-SG01']='10.108.56.223'
addresses['HGST-S3-DC03-R01-SG01']='10.108.56.224'


for i in devices.keys():
    nicUpdate = {}
    nicUpdate['address']= addresses[i]
    nicUpdate['netmask']='255.255.254.0'
    nicUpdate['network']=net_guid
    devices[i]['nicUpdate'] = nicUpdate


pprint.pprint(devices)
    
# push the new data
for i in devices.keys():
    message = '/model/machine/%s/nic/%s' % (i, devices[i]['nic_guid'])
    print message
    print ha.put(message, data = json.dumps(devices[i]['nicUpdate']))


tasks = []    
# reconfigure the host
for i devices.keys():
    tasks.append(cli.marvin.machine.configure(i))


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
