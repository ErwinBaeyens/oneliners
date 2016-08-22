from marvin_lib.task  import wait_for_tasks
import json

# trigger the health check on all machines
for machine in cli.marvin.machine.list():
    if not machine['status'] == 'ONLINE':
        print "Machine {} is not ONLINE".format(machine['name'])
    else:
        task = cli.marvin.machine.health_check(machine['guid'])
        wait_for_tasks([task])


        # Analyse results
        output = cli.marvin.task.result(task['guid'])
        result = json.loads(output)['result']
        for test, test_result in result.iteritems():
            if not test_result['result']:
                print "Test {} failed on machine {}".format(test, machine['name'])
                
