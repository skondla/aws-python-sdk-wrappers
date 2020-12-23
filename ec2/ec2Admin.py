#!/usr/bin/env python
# Author: Sudheer Kondla, 04/21/17, skondla@me.com
# Purpose: EC2 Instance Administration

import boto3
import sys
#import jsbeautifier
#import js-beautify
#Afrom jsbeautifier import js-jsbeautifier

def create_ami_image(instanceId,imageName,imageDescription):
    """
    Create AMI based on specific Instance Id
    """
    client = boto3.client('ec2')
    response = client.create_image(
        InstanceId=instanceId,
        Name=imageName,
        Description=imageDescription,
        BlockDeviceMappings=[
            {
                'DeviceName': '/dev/xvda',
                'Ebs': {
                    'VolumeSize': 10,
                    'DeleteOnTermination': False,
                    'VolumeType': 'gp2'
                }
            },
            {
                'DeviceName': '/dev/xvdb',
                'Ebs': {
                    'VolumeSize': 20,
                    'DeleteOnTermination': True,
                    'VolumeType': 'gp2'
                }
            },
        ]
    )
    print(response)

def copy_ami_image(sourceRegion,sourceImageId,imageName,imageDescription):
    client = boto3.client('ec2')
    response = client.copy_image(
        SourceRegion=sourceRegion,
        SourceImageId=sourceImageId,
        Name=imageName,
        Description=imageDescription
    )
    print(response)

def describe_images(imageId):
    client = boto3.client('ec2')
    response = client.describe_images(
        ImageIds=imageId
    )
    print(response)

def create_volume(az,size,volumeType):
    client = boto3.client('ec2')
    response = client.create_volume(
        AvailabilityZone=az,
		Size=size,
        VolumeType=volumeType,
    )
    #VolumeType='standard'|'io1'|'gp2'|'sc1'|'st1'
    print(response)

def attach_volume(volumeId,instanceId,deviceName):
    client = boto3.client('ec2')
    response = client.attach_volume(
        VolumeId=volumeId,
        InstanceId=instanceId,
        Device=deviceName
    )
    #Device=/dev/xvda OR /dev/svda
    print(response)

def detach_volume(volumeId,instanceId):
    client = boto3.client('ec2')
    response = client.detach_volume(
        InstanceId=instanceId,
        VolumeId=volumeId,
    )
    

def create_ec2_instances(amiId,minInst,maxInst,instantType,keyName,securityGrpIds,subnetId,tagValue):
    client = boto3.client('ec2')
    response = client.run_instances(
        ImageId=amiId,
        MinCount=minInst,
        MaxCount=maxInst,
        KeyName=keyName,
        SecurityGroupIds=[
            securityGrpIds,
        ],
        UserData='#!/bin/bash \
        apt-get update \
        apt-get install python-pip \
        apt-get install boto3 \
        apt-get install vim \
        apt-get install bc \
        apt-get install sysstat',
        InstanceType=instantType,
        SubnetId=subnetId,
        AssociatePublicIpAddress=True,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'name',
                        'Value': tagValue
                    },
                ]
            },
        ]

    )
    print(response)

def stop_instance(instanceId):
    client = boto3.client('ec2')
    response = client.stop_instances(
      InstanceIds=[
            instanceId,
        ],
        Force=True
    )
    print(response)

#http://boto3.readthedocs.io/en/latest/reference/services/ec2.html?highlight=EC2#EC2.Client.modify_instance_attribute
# Attribute='instanceType'|'kernel'|'ramdisk'|'userData'|'disableApiTermination'|'instanceInitiatedShutdownBehavior'|'rootDeviceName'|'blockDeviceMapping'|'productCodes'|'sourceDestCheck'|'groupSet'|'ebsOptimized'|'sriovNetSupport'|'enaSupport',
def modify_instance_attribute(instanceId,instanceType):
    client = boto3.client('ec2')
    response = client.stop_instances(
        DryRun=False,
        InstanceId=instanceId,
        InstanceType=
		{
		    'Value': instanceType
		}
    )
    print(response)
