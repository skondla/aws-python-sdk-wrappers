#!/usr/bin/env python3
from ec2Admin import attach_volume
from datetime import date
#import js-beautify

import sys

if len(sys.argv)<4:
    print 'Please enter volumeId,instanceId,deviceName !!!Exiting !!!'
    exit()

today = date.today()
volumeId=sys.argv[1]
instanceId = sys.argv[2]
deviceName = sys.argv[3]

if __name__ == '__main__':
    attach_volume(volumeId,instanceId,deviceName)
