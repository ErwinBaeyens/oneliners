from marvin_lib.task import wait_for_tasks
from marvin_lib.network import ha

import json

upgradetar_key = "upgrade_blackbanner-ms88_blackbanner-ms90.tar"

column_name = cli.marvin.column.list()[0]['name']
s_guid = cli.marvin.environment.list()[0]['guid']
task = cli.marvin.environment.process_upgrade_image(s_guid, path=upgradetar_key)
wait_for_tasks([task['guid']])


#
# check avialable versions
#
s_guid = cli.marvin.environment.list()[0]['guid']
cli.marvin.environment.list_available_versions(s_guid)

#start the upgrade
target_version = 'ActiveScale 5.0.90'
cli.marvin.environment.upgrade(s_guid, target_version=target_version, health_check=False)


# check progress

#  scaler
print ha.get('/model/task/?query="action=upgrade%26tasktype=taskgroup%26resourcetype=environment"')
