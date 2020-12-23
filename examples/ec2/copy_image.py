#!/usr/bin/env python3
from ec2Admin import copy_ami_image
from datetime import date
#import js-beautify

import sys

if len(sys.argv)<5:
    print ('Please enter sourceRegion, sourceImageId, imageName, imageDescription.  !!!Exiting !!!')
    exit()

today = date.today()
sourceRegion=sys.argv[1]
sourceImageId=sys.argv[2]
imageName = sys.argv[3]
imageDescription = sys.argv[4]
#imageDescription = imageName + "-" + str(today) + "-" + sourceRegion 
#profile = sys.argv[3]

if __name__ == '__main__':
    copy_ami_image(sourceRegion,sourceImageId,imageName,imageDescription)
