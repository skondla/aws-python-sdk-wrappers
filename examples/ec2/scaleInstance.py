#!/usr/bin/env python3
from ec2Admin import modify_instance_attribute
from datetime import date
#import js-beautify

import sys

if len(sys.argv)<3:
    print ('Please enter instanceId,instanceType !!!Exiting !!!')
    exit()

today = date.today()
instanceId=sys.argv[1]
instanceType=sys.argv[2]

if __name__ == '__main__':
    modify_instance_attribute(instanceId,instanceType)
