#!/usr/bin/python
from datetime import timedelta
import sys, os
import pytz

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..')) # ugly hack to allow import from the root
from fabfile.failover import clients, servers, AT


#########################
db = 'couchbase2'
wl = 'A'
e2 = servers[1]

NODE_STOP_TIME = 600 #In secs.
NODE_RESTART_TIME = 1200 #In secs.

at = AT(db)
# start workload
at[0].client_run(clients, db, wl, 250000)

# kill server
#at[600].server_kill([e1], db)
at[NODE_STOP_TIME].server_kill([e2], db)

# the server is up back
#at[1200].server_start([e1], db)
at[NODE_RESTART_TIME].server_start([e2], db)

at.fire()