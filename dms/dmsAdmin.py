#!/usr/bin/env python
# Author: Sudheer Kondla, 02/13/18, skondla@me.com
# Purpose: Database Migration Service (DMS) Administration

import boto3
import sys
#import jsbeautifier
#import js-beautify
#Afrom jsbeautifier import js-jsbeautifier

def create_replication_instance(dmslInstName,allocStorage,dmsInstClass):
    """
    Create DMS Instance
    DMS Instance Types: dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
    | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge
    """
    client = boto3.client('dms')
    response = client.create_replication_instance(
        ReplicationInstanceIdentifier=dmslInstName,
        AllocatedStorage=allocStorage,
        ReplicationInstanceClass=dmsInstClass,
        Tags=[
         {
            'Key': 'Name',
            'Value': 'DMS Instance'
         },
       ],
        MultiAZ=False,
        PubliclyAccessible=False,
        ReplicationSubnetGroupIdentifier='sg-e85f4f8e'
        #VpcSecurityGroupIds=['sg-f1989796'],
        #VpcSecurityGroupIds=['sg-e85f4f8e', 'sg-f1989796']
    )
    print(response)

def delete_replication_instance(dmslInstARN):
    """
    Delete DMS Instance
    """
    client = boto3.client('dms')
    response = client.delete_replication_instance(
        ReplicationInstanceArn=dmslInstARN
    )
    print(response)