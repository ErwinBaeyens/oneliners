# list all users that are defined on a scaler system

from scalerim_api.constants import SIM_IdentityFilter

t_filter = SIM_IdentityFilter(True, True)
accounts = cli.clients.scalerim.identityPageGet('','', True, True, 100, t_filter)

for account in accounts:
    print "\t%s\t%s\t%s"%(account.displayName, account.email, account.canonicalId)

    
