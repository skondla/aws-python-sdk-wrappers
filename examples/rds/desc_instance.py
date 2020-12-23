#!/usr/bin/env python
from rdsAdmin import rds_desc_db_instances

import sys

if len(sys.argv)<2:
    print ('Please enter DB Instance Name.  !!!Exiting !!!')
    exit()
instanceName = sys.argv[1]
#profile = sys.argv[3]

if __name__ == '__main__':
    rds_desc_db_instances(instanceName)

