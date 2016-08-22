from marvin_lib.task import wait_for_tasks
import json

for machine in cli.marvin.machine.list():
    print '\n', machine['name']
    for nic in machine['nic']:
        if nic['address'] != None:
            print nic['device'], nic['address'], nic['macaddress']
    print '\n'

    
