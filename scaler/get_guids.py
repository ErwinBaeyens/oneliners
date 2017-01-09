# You can retrieve the guids using a marvin ha get call as well, and that would be cleaner and more reliable
# Also, in testhelpers 0.3; all guids are immediatly available as well.
# example for testhelpers 0.2 with ha:
class yadda(object):
  def __init__(self):
        
    machines = self.ha.get_retry('/model/machine')['machine']
    # will return a list of the dictionary machines of the marvin model for scaler
    for m in machines:
      print m['guid'], m['role'], m['name']
    
      # That  will print all guids, roles and names
      # To retrieve all backend nodes:
      # First take an intermediate step for getting all columns:
      # This will also work for scale-up and scale-out !
            
      cols = self.ha.get_retry('/model/column')['column']
      all_machines = []
      for column in cols:
        machines = self.ha.get_retry('/model/column/{}/action/proxy/machine'.format(column['guid']))['machine']
        all_machines.extend(machines)

    
