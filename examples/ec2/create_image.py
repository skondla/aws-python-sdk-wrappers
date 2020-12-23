#!/usr/bin/env python3
from ec2Admin import create_ami_image
from datetime import date
#import js-beautify

import sys

if len(sys.argv)<4:
    print ('Please enter instanceId,  imageName, imageDescription.  !!!Exiting !!!')
    exit()

today = date.today()
instanceId=sys.argv[1]
imageName = sys.argv[2]
imageDescription = sys.argv[3]
#imageDescription = imageName + "-" + str(today) + "-" + instanceId 
#profile = sys.argv[3]

if __name__ == '__main__':
    create_ami_image(instanceId,imageName,imageDescription)
