#!/usr/bin/env python3
from ec2Admin import create_volume
from datetime import date
#import js-beautify

import sys

if len(sys.argv)<4:
    print ('Please enter az,volumeType,size !!!Exiting !!!')
    exit()

today = date.today()
az=sys.argv[1]
size = int(sys.argv[2])
volumeType = sys.argv[3]

if __name__ == '__main__':
    create_volume(az,size,volumeType)
