#!/usr/bin/env python3
#Author: skondla@me.com

import boto3
import botocore
from botocore.exceptions import ClientError

def getPassword(region,key):
    ''' Get secret key value [for example DB password] for use by apps & and users '''
    try:
        client = boto3.client('secretsmanager',region_name=region)
        response = client.get_secret_value(
            SecretId=key
        )
        return response['SecretString']
    except botocore.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        print(error_code)
        if error_code == '404':
            print('Secret Name: ' +  secret_name + ' does not exists!!')

def setPassword(region,key,value):
    ''' Update en existing secret key '''
    try:
        client = boto3.client('secretsmanager',region_name=region)
        response = client.put_secret_value(
            SecretId=key,
            SecretString=str(value)
        )
    except botocore.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        print(error_code)
        if error_code == '404':
            print('Secret Value: ' +  str(value) + ' cannot be updated')

def createSecret(region,key,value):
    '''Create new Secret key '''
    try:
        client = boto3.client('secretsmanager',region_name=region)
        response = client.create_secret(
            Name=key,
            SecretString=value,
            Tags=[
                {
                    'Key': 'name',
                    'Value': 'database-password'
                },
            ]
        )
    except botocore.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        print(error_code)
        if error_code == '404':
            print('Secret : ' +  str(key) + ' cannot be created or may already exists')

def deleteSecret(region,key):
    '''' Delete Secret Key with 30 days recovery time'''
    try:
        client = boto3.client('secretsmanager',region_name=region)
        response = client.delete_secret(
            SecretId=key,
            RecoveryWindowInDays=30,
        )
    except botocore.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        print(error_code)
        if error_code == '404':
            print('Secret Value: ' +  str(value) + ' cannot be deleted')

def deleteSecretForce(region,key):
    '''' Delete Secret Key with 30 days recovery time'''
    try:
        client = boto3.client('secretsmanager',region_name=region)
        response = client.delete_secret(
            SecretId=key,
            ForceDeleteWithoutRecovery=True,
        )
    except botocore.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        print(error_code)
        if error_code == '404':
            print('Secret Value: ' +  str(value) + ' cannot be deleted')

def restoreSecret(region,key):
    ''' Secret Key can be restored if deleted with 30 days '''
    try:
        client = boto3.client('secretsmanager',region_name=region)
        response = client.restore_secret(
            SecretId=key
        )
    except botocore.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        print(error_code)
        if error_code == '404':
            print('Secret Value: ' +  str(value) + ' cannot be deleted')

def listSecrets(region,key):
    ''' List Secrets from SecretManager'''
    try:
        client = boto3.client('secretsmanager',region_name=region)
        response = client.list_secrets(            
        )
    except botocore.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        print(error_code)
        if error_code == '404':
            print('Secret Values: cannot be listed')