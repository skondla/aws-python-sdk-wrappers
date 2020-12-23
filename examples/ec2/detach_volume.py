#!/usr/bin/env python
from ec2Admin import detach_volume
from datetime import date
#import js-beautify

import sys

if len(sys.argv)<3:
    print ('Please enter volumeId,instanceId !!!Exiting !!!')
    exit()

today = date.today()
volumeId=sys.argv[1]
instanceId = sys.argv[2]
#deviceName = sys.argv[3]

if __name__ == '__main__':
    detach_volume(volumeId,instanceId)
