import i


api=i.confi.cloudApiConnection.find('main')
list_sn = api.machine.list(machinerole='STORAGENODE')['result']
guids = [x['guid'] for x in list_sn]

for guid in guids:
    api.machine.reboot(guid)
