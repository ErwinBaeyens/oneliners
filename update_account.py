from scalerim_api.constants import SIM_IdentityFilter

# set up the filter
t_filter = SIM_IdentityFilter(True, True)

# get a list of the available accounts
accounts = cli.clients.scalerim.identityPageGet('ctx','', True, True, 100, t_filter)

# and show them
for account in accounts:
    print "%s\t%s\t%s"%(account.displayName, account.email, account.canonicalId)

# select the account you want
account =  accounts[1]

# modify the properties
account.email = 'new_email@address.com'

# push the changes
cli.clients.scalerim.identityUpdate('', account.canonicalId, account.displayName,
                                    account.email, account.enabled)
