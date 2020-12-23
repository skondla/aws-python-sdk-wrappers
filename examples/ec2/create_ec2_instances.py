#!/usr/bin/env python3
from ec2Admin import create_ec2_instances
from datetime import date
#import js-beautify

import sys

if len(sys.argv)<9:
    print ('Please enter amiId,minInst,maxInst,instantType,keyName,securityGrpIds,subnetId,tagValue.  !!!Exiting !!!')
    exit()

today = date.today()
amiId=sys.argv[1]
minInst = sys.argv[2]
maxInst = sys.argv[3]
instantType = sys.argv[4]
keyName = sys.argv[5]
securityGrpIds = sys.argv[6]
subnetId = sys.argv[7]
tagValue = sys.argv[8]
#maxInst = minInst + "-" + str(today) + "-" + amiId 
#profile = sys.argv[3]

if __name__ == '__main__':
    #create_ec2_instances(amiId,minInst,maxInst)
	create_ec2_instances(amiId,minInst,maxInst,instantType,keyName,securityGrpIds,subnetId,tagValue)
