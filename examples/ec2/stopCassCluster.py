#!/usr/bin/env python3
import boto3
import sys
from ec2Admin import stop_instance

if len(sys.argv) < 2:
    print ("You must set argument!!!")

instanceId=str(sys.argv[1])
if __name__ == '__main__':
   stop_instance(instanceId) 
