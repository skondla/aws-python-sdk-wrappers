#!/usr/bin/env python3
#Author: Sudheer Kondla, skondla@me.com 
#Purpose: AWS Simple Storage Service Administration
# -*- coding: utf-8 -*-

import boto3
import sys
import botocore
from botocore.exceptions import ClientError
from boto3.s3.transfer import S3Transfer
import json

class UploadS3:
    def __init__(self):
        pass

    #@staticmethod    
    #def upload_file(self, fileName,bucketName,fileAlias):
    def upload_file(self, **kwargs):
        s3 = boto3.resource('s3')
        try:
            s3 = boto3.resource('s3')
            s3.meta.client.upload_file(kwargs[0], kwargs[1], kwargs[2])
        except ClientError as e:
		    # If it was a 404 error, then the bucket does not exist.
            error_code = e.response['Error']['Code']
            print(error_code)
            if error_code == '404':
                print('Bucket: ' +  kwargs[1] + ' does not exists!!')

    #@staticmethod
    def transfer2S3(self, *args):
        try:
            s3 = boto3.resource('s3')
            client = s3.meta.client
            #transfer = S3Transfer(client,'us-east-1')
            transfer = S3Transfer(client)
            transfer.upload_file(args[0],
                     args[1],
                     args[2],
                     extra_args={'ServerSideEncryption': 'AES256'})
        except ClientError as e:
            error_code = e.response['Error']['Code']
            print(error_code)
            if error_code == '404':
                print('Uploading to bucket: ' + args[1] + ' failed!!')

class CreateS3:
    def __init__(self):
        pass

    @staticmethod
    def createBucketUS(bucketName):
        client = boto3.client('s3')
        response = client.create_bucket(
            ACL='private',
            Bucket=bucketName
        )
        print (response)
    
    @staticmethod
    def createBucket(bucketName, region):
        client = boto3.client('s3')
        response = client.create_bucket(
            ACL='private',
            Bucket=bucketName,
            CreateBucketConfiguration={
                'LocationConstraint': region
            }
        )
        print (response)

    @staticmethod
    def createBucketPolicy(*kwargs):
        s3 = boto3.client('s3')
        bucketName = kwargs[0]
        print("From createBucketPolicy(), Bucket Name: " + bucketName)
        bucket_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "AddPerm",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": "s3:*",
                    "Resource": "arn:aws:s3:::%s/*" %bucketName,
                    "Condition": {
                        "IpAddress": {
                        "aws:SourceIp": [
                            "10.200.0.0/16",
                            "4.35.2.52/32",
                            "4.35.2.66/32"
                            ]
                        }
                    }
                }
            ]
        }
        bucket_policy = json.dumps(bucket_policy)
        s3.put_bucket_policy(Bucket=bucketName, Policy=bucket_policy)
        
class CheckS3:
    def __init__(self):
        pass
        
    def check_bucket(self,bucket):    		
        try:
            s3 = boto3.resource('s3')
            s3.meta.client.head_bucket(Bucket=bucket)
            print("Bucket: " + bucket + " exists!")
            return True
        except botocore.exceptions.ClientError as e:
            # If a client error is thrown, then check that it was a 404 error.
            # If it was a 404 error, then the bucket does not exist.
            error_code = int(e.response['Error']['Code'])
            if error_code == 403:
                print("Private Bucket. Forbidden Access!")
                return True
            elif error_code == 404:
                print("Bucket:" + bucket + " does Not Exist!")
                return False

class EncryptS3:
    def __init__(self):
        pass 
    def encryptBucket(self, bucketName):
        print("Bucket Name from encryptBucket: " + str(bucketName))
        try:
            client = boto3.client('s3')
            response = client.put_bucket_encryption(
                Bucket=str(bucketName),
                ServerSideEncryptionConfiguration={
                    'Rules': [
                        {
                            'ApplyServerSideEncryptionByDefault': {
                                'SSEAlgorithm': 'AES256',
                                }
                        },
                    ]
                }
            )   
            return True
        except botocore.exceptions.ClientError as e:
            error_code = int(e.response['Error']['Code'])
            if error_code == 403:
                print("Private Bucket. Forbidden Access!")
                return True
            elif error_code == 404:
                print("Bucket:" + kwargs[0] + " cannot be encrypted")
                return False



