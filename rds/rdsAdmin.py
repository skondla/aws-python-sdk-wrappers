#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Sudheer Kondla, 04/21/17, Sudheer.Kondla@ibm.com
# Purpose: RDS Instance Administration

import boto3
import sys
#import jsbeautifier
#import js-beautify
#from jsbeautifier import js-jsbeautifier

class RDSCreate:

    def rds_create_db_cluster_snapshot(self, snapshotName, dbname, tagName):
        client = boto3.client('rds')
        response = client.create_db_cluster_snapshot(DBClusterSnapshotIdentifier=snapshotName, DBClusterIdentifier=dbname,
                                                 Tags=[{'Key': 'Name', 'Value': tagName}, ])
        print(response)


    def rds_create_db_snapshot(self, snapshotName, dbname, tagName):
        client = boto3.client('rds')
        response = client.create_db_snapshot(DBSnapshotIdentifier=snapshotName, DBInstanceIdentifier=dbname,
                                         Tags=[{'Key': 'Name', 'Value': tagName}, ])
        print(response)

    def create_db_instance_read_replica(self, replicaName, sourceDBName, az):
        # session = boto3.Session(profile_name=profile)
        # Any clients created from this session will use credentials
        # from the [default] section of ~/.aws/credentials.
        # client = session.client('rds')
        client = boto3.client('rds')
        response = client.create_db_instance_read_replica(DBInstanceIdentifier=replicaName,
                                                          SourceDBInstanceIdentifier=sourceDBName,
                                                          AvailabilityZone=az)
        print(response)

    def create_db_cluster_parameter_group_tag(self, dbClusterParmGrp, dbParamGrpFamily, description, tagKeyField,
                                          tagKeyValue):
        client = boto3.client('rds')
        response = client.create_db_cluster_parameter_group(
            DBClusterParameterGroupName=dbClusterParmGrp,
            DBParameterGroupFamily=dbParamGrpFamily,
            Description=description,
            Tags=[
                {
                    'Key': tagKeyField,
                    'Value': tagKeyValue
                },
            ]
        )
        print(response)

    def create_db_cluster_parameter_group(self, dbClusterParmGrp, dbParamGrpFamily, description):
        client = boto3.client('rds')
        response = client.create_db_cluster_parameter_group(
            DBClusterParameterGroupName=dbClusterParmGrp,
            DBParameterGroupFamily=dbParamGrpFamily,
            Description=description
        )
        print(response)

    def create_db_parameter_group2(self, dbParamGrpName, dbParamGrpFamily, description, tagKeyField, tagKeyValue):
        client = boto3.client('rds')
        response = client.create_db_parameter_group(
            DBParameterGroupName=dbParamGrpName,
            DBParameterGroupFamily=dbParamGrpFamily,
            Description=description,
            Tags=[
                {
                    'Key': tagKeyField,
                    'Value': tagKeyValue
                },
            ]
        )
        print(response)

    def create_db_parameter_group(self, dbParamGrpName, dbParamGrpFamily, description):
        client = boto3.client('rds')
        response = client.create_db_parameter_group(
            DBParameterGroupName=dbParamGrpName,
            DBParameterGroupFamily=dbParamGrpFamily,
            Description=description
        )
        print(response)

    def create_db_instance(self, engine,instanceName,instanceClass,dbSubnetGrp,user,password,storageSize,storageType,dbSecurityGrp,kmsKeyId,engineVersion):
        client = boto3.client('rds')
        response = client.create_db_instance(
            DBInstanceClass=instanceClass,
            DBInstanceIdentifier=instanceName,
            Engine=engine,
            EngineVersion=engineVersion,
            DBSubnetGroupName=dbSubnetGrp,
            MasterUsername=user,
            MasterUserPassword=password,
            AllocatedStorage=storageSize,
            StorageType=storageType,
            StorageEncrypted=True,
            KmsKeyId=kmsKeyId,
            VpcSecurityGroupIds=[
                dbSecurityGrp,
            ],
        )
        print(response)

    def create_cluster_db_instance(self, *kwargs):
        client = boto3.client('rds')
        response = client.create_db_instance(
            DBInstanceIdentifier=kwargs[0],
            Engine=kwargs[1],
            EngineVersion=kwargs[2],
            DBSubnetGroupName=kwargs[3],
            VpcSecurityGroupIds=[
                kwargs[4],
            ],
            DBInstanceClass=kwargs[5],
	    DBClusterIdentifier=kwargs[6]	
        )
        print(response)
class RDSDelete:
    def rds_delete_db_cluster_snapshot(self, snapshotName):
        client = boto3.client('rds')
        response = client.delete_db_cluster_snapshot(DBClusterSnapshotIdentifier=snapshotName)
        print(response)

    def delete_db_snapshot(self,dbSnapshotName):
        client = boto3.client('rds')
        response = client.delete_db_snapshot(
            DBSnapshotIdentifier=dbSnapshotName
        )
        print(response)
        # def delete_db_instance(dbInstance,skipFinalSnap,finalSnapshotName):

    def delete_db_instance(self, dbInstance, finalSnapshotName):
    #def delete_db_instance(dbInstance,skipFinalSnap,finalSnapshotName):
        client = boto3.client('rds')
        response = client.delete_db_instance(
            DBInstanceIdentifier=dbInstance,
            #SkipFinalSnapshot=str(skipFinalSnap)
            #SkipFinalSnapshot=bool(skipFinalSnap)
            FinalDBSnapshotIdentifier=finalSnapshotName
        )
        print(response)

    def delete_db_instance_replica(self, dbInstance, skipFinalSnap):
        client = boto3.client('rds')
        response = client.delete_db_instance(
            DBInstanceIdentifier=dbInstance,
            SkipFinalSnapshot=bool(skipFinalSnap)
        )
        print(response)

    #def delete_cluster_db_instance(self, dbInstance, skipFinalSnap):
    #def delete_cluster_db_instance(self, dbInstance, finalSnapshotName):
    def delete_cluster_db_instance(self, dbInstance):
        client = boto3.client('rds')
        response = client.delete_db_instance(
            DBInstanceIdentifier=dbInstance,
            SkipFinalSnapshot=False
      #      FinalDBSnapshotIdentifier=finalSnapshotName
        )
        print(response)

    def delete_db_cluster(self, dbClusterName, finalSnapshotName):
        client = boto3.client('rds')
        response = client.delete_db_cluster(
            DBClusterIdentifier=dbClusterName,
            FinalDBSnapshotIdentifier=finalSnapshotName
        )
        print(response)

    # def delete_db_cluster(dbClusterName,skipFinalSnap,finalSnapshotName):
    #    client = boto3.client('rds')
    #    response = client.delete_db_cluster(
    #        DBClusterIdentifier=dbClusterName,
    #        SkipFinalSnapshot=skipFinalSnap,
    #        FinalDBSnapshotIdentifier=finalSnapshotName
    #    )
    #    print(response)

class RDSDescribe:
    def dbInstanceInfo(self,instanceName):
    	if 'cluster' in instanceName:
        	#print (instanceName + ' is a cluster')
		instanceName=instanceName.split('.')[0]
		client = boto3.client('rds')
        	response = client.describe_db_clusters(
                	DBClusterIdentifier=instanceName)
		getDBInfo = list()
		getDBInfo.append(response['DBClusters'][0]['VpcSecurityGroups'][0]['VpcSecurityGroupId'])
		getDBInfo.append(response['DBClusters'][0]['DBSubnetGroup'])
		getDBInfo.append(response['DBClusters'][0]['Engine'])
		getDBInfo.append(response['DBClusters'][0]['DatabaseName'])
		getDBInfo.append(response['DBClusters'][0]['EngineVersion'])
		#getDBInfo.append(response['DBClusters'][0]['DBInstanceClass'])
		print(getDBInfo)
    	else:
		instanceName=instanceName.split('.')[0]
		client = boto3.client('rds')
		response = client.describe_db_instances(DBInstanceIdentifier=instanceName)
		getDBInfo = list()
		getDBInfo.append(response['DBInstances'][0]['VpcSecurityGroups'][0]['VpcSecurityGroupId'])
		#getDBInfo.append(response['DBInstances'][0]['DBSubnetGroup'][0]['DBSubnetGroupName'])
		#getDBInfo.append(response['DBInstances'][0]['Endpoint'][0]['Address'])
		#getDBInfo.append(response['DBInstances'][0]['DBParameterGroups'][0]['DBParameterGroupName'])
		#getDBInfo.append(response['DBInstances'][0]['DBSubnetGroup'][0]['Subnets'][0]['SubnetAvailabilityZone'])
		getDBInfo.append(response['DBInstances'][0]['DBSubnetGroup']['DBSubnetGroupName'])
		getDBInfo.append(response['DBInstances'][0]['Engine'])
		getDBInfo.append(response['DBInstances'][0]['DBName'])
		getDBInfo.append(response['DBInstances'][0]['EngineVersion'])
		getDBInfo.append(response['DBInstances'][0]['DBInstanceClass'])
		print(getDBInfo)

    def rds_desc_db_instances(self, dbname):
        client = boto3.client('rds')
        response = client.describe_db_instances(DBInstanceIdentifier=dbname)
        print(response)

    def describe_db_cluster_snapshots(self, snapshotName):
        client = boto3.client('rds')
        response = client.describe_db_cluster_snapshots(
            DBClusterSnapshotIdentifier=snapshotName,
            #SnapshotType='automated',
        )
    	print(response)
    #jsbeautifier response
    def rds_desc_db_instances_all(self):
        client = boto3.client('rds')
        response = client.describe_db_instances()
        print(response)

    #def describe_db_clusters(self, dbClusterName):
    #    client = boto3.client('rds')
    #    response = client.describe_db_clusters(
    #        DBClusterIdentifier=dbClusterName)
    #    print(response)
    def describe_db_clusters(self,dbClusterName):
    	client = boto3.client('rds')
    	response = client.describe_db_clusters(
        	DBClusterIdentifier=dbClusterName)
    	print(response)

 	

    #def describe_db_clusters(dbClusterName,accesskey,SecretKey,profile,region):
    #    client = boto3.client('rds',aws_access_key_id=accesskey,
    #    aws_secret_access_key=SecretKey,profile_name=profile,region_name=region
    #    )
    #    response = client.describe_db_clusters(
    #        DBClusterIdentifier=dbClusterName)
    #    print(response)

    def describe_db_clusters2(self, dbClusterName,profile,region):
        # Any clients created from this session will use credentials
        # from the [default] section of ~/.aws/credentials.
        session = boto3.Session(profile_name=profile,region_name=region)
        client = session.client('rds')
        response = client.describe_db_clusters(
            DBClusterIdentifier=dbClusterName)
        print(response)

    def describe_events(self, dbName,sourceType,startTime,endTime,duration):
        client = boto3.client('rds')
        response = client.describe_events(
            SourceIdentifier=dbName,
            SourceType=sourceType,
            StartTime=startTime,
            EndTime=endTime,
            Duration=duration)
            # Default Duration: 60 minutes
            # http://boto3.readthedocs.io/en/latest/reference/services/rds.html?highlight=rds#RDS.Client.describe_events
        print(response)

    def describe_events2(self, dbName,sourceType,duration):
        client = boto3.client('rds')
        response = client.describe_events(
            SourceIdentifier=dbName,
            SourceType=sourceType,
            Duration=duration)
            # Default Duration: 60 minutes
            # http://boto3.readthedocs.io/en/latest/reference/services/rds.html?highlight=rds#RDS.Client.describe_events
        print(response)
    def describe_db_snapshots(self, dbSnapshotName):
        client = boto3.client('rds')
        response = client.describe_db_snapshots(
        DBSnapshotIdentifier=dbSnapshotName
        )
        print(response)

class RDSAvailability:
    def reboot_db_instance(self, dbInstanceName,forceFailover):
        client = boto3.client('rds')
        response = client.reboot_db_instance(
            DBInstanceIdentifier=dbInstanceName)#,
            #ForceFailover=forceFailover
        print(response)

    def failover_db_cluster(self, dbClusterName,targetDBInstanceName):
        client = boto3.client('rds')
        response = client.failover_db_cluster(
            DBClusterIdentifier=dbClusterName,
            TargetDBInstanceIdentifier=targetDBInstanceName
        )
        print(response)

class RDSEncrypt:
    def encrypt_db_snapshot(self, sourceDBSnap,targetDBSnap,kmsKeyId):
        client = boto3.client('rds')
        response = client.copy_db_snapshot(
            SourceDBSnapshotIdentifier=sourceDBSnap,
            TargetDBSnapshotIdentifier=targetDBSnap,
        #Encrypted=True,
            KmsKeyId=kmsKeyId
        )
        print(response)

class RDSCopy:
    def copy_db_snapshot(self, sourceDBSnap,targetDBSnap,kmsKeyId,keyName,keyValue,copyTags,sourceRegion):
        client = boto3.client('rds')
        response = client.copy_db_snapshot(
            SourceDBSnapshotIdentifier=sourceDBSnap,
            TargetDBSnapshotIdentifier=targetDBSnap,
            KmsKeyId=kmsKeyId,
            Tags=[
                {
                    'Key': keyName,
                    'Value': keyValue
                },
            ],
            CopyTags=copyTags,
            SourceRegion=sourceRegion
        )
        print(response)

    #def copy_db_snapshot(self, sourceDBSnap,targetDBSnap,sourceRegion):
    #    client = boto3.client('rds')
    #    response = client.copy_db_snapshot(
    #        SourceDBSnapshotIdentifier=sourceDBSnap,
    #        TargetDBSnapshotIdentifier=targetDBSnap,
    #        SourceRegion=sourceRegion
    #    )
    #    print(response)

    def copy_db_snapshot_encrypt(self, sourceSnap, encryptSnap, kmsKeyId):
        client = boto3.client('rds')
        response = client.copy_db_snapshot(
            SourceDBSnapshotIdentifier=sourceSnap,
            TargetDBSnapshotIdentifier=encryptSnap,
            KmsKeyId=kmsKeyId
        )
        print(response)

    #def copy_db_snapshot(self, sourceSnap, targetSnap):
    #    client = boto3.client('rds')
    #    response = client.copy_db_snapshot(
    #        SourceDBSnapshotIdentifier=sourceSnap,
    #        TargetDBSnapshotIdentifier=targetSnap
    #    )
    #    print(response)

    def copy_db_cluster_snapshot_encrypt(self, sourceSnap, encryptSnap, kmsKeyId):
        client = boto3.client('rds')
        response = client.copy_db_snapshot(
            SourceDBSnapshotIdentifier=sourceSnap,
            TargetDBSnapshotIdentifier=encryptSnap,
            KmsKeyId=kmsKeyId
        )
        print(response)

    def copy_db_cluster_snapshot(self, sourceSnap, targetSnap):
        client = boto3.client('rds')
        response = client.copy_db_snapshot(
            SourceDBSnapshotIdentifier=sourceSnap,
            TargetDBSnapshotIdentifier=targetSnap
        )
        print(response)

    def copy_cross_region_db_cluster_snapshot(self, sourceSnap, targetSnap,tagValue,sourceReg,targetReg,kmsKey):
        client = boto3.client('rds',targetReg)
        response = client.copy_db_cluster_snapshot(
            SourceDBClusterSnapshotIdentifier=sourceSnap,
            TargetDBClusterSnapshotIdentifier=targetSnap,
	        CopyTags=True,
        	Tags=[
                {
                    'Key': 'name',
                    'Value': tagValue
                }
            ],
            SourceRegion=sourceReg,	
            KmsKeyId=kmsKey
        )
        print(response)

    def copy_cross_region_db_snapshot(self, *kwargs):
        client = boto3.client('rds',kwargs[4])
        response = client.copy_db_snapshot(
            SourceDBSnapshotIdentifier=kwargs[0],
            TargetDBSnapshotIdentifier=kwargs[1],
	        CopyTags=True,
        	Tags=[
                {
                    'Key': 'name',
                    'Value': kwargs[2]
                }
            ],
            SourceRegion=kwargs[3],	
            KmsKeyId=kwargs[5]
        )
        print(response)

class RDSModify:
    def modify_db_parameter_group(self, dbParamGrpName,applyMethod,paramName,paramValue):
        client = boto3.client('rds')
        response = client.modify_db_parameter_group(
            DBParameterGroupName=dbParamGrpName,
            Parameters=[
                {
                    'ApplyMethod': applyMethod,
                    'ParameterName': paramName,
                    'ParameterValue': paramValue,
                },
            ],
        )
        print(response)

    def modify_db_cluster_parameter_group(self, dbClusterParmGrp,applyMethod,paramName,paramValue):
        client = boto3.client('rds')
        response = client.modify_db_parameter_group(
            DBParameterGroupName=dbClusterParmGrp,
            Parameters=[
                {
                    'ApplyMethod': applyMethod,
                    'ParameterName': paramName,
                    'ParameterValue': paramValue,
                },
            ],
        )
        print(response)

    #def restore_db_cluster_from_s3():
    #def restore_db_cluster_from_snapshot():
    #def restore_db_instance_from_db_snapshot():

    def modify_db_instance_class(self, dbInstanceName,paramValue):
        client = boto3.client('rds')
        response = client.modify_db_instance(
            DBInstanceIdentifier=dbInstanceName,
            DBInstanceClass=paramValue)
        print(response)

class RDSRestore:
    def restore_db_instance_from_db_snapshot(self, *kwargs):
        client = boto3.client('rds')
        response = client.restore_db_instance_from_db_snapshot(
            DBInstanceIdentifier=kwargs[0],
            DBSnapshotIdentifier=kwargs[1],
            PubliclyAccessible=False,
            DBSubnetGroupName=kwargs[2],
            #VpcSecurityGroupIds=kwargs[3],
            VpcSecurityGroupIds=[
                kwargs[3],
            ],
            Engine=kwargs[4],
	    #EngineVersion=kwargs[5],
	    #DBInstanceClass=kwargs[6]	
	    DBInstanceClass=kwargs[5]	
        )
        print(response)
    
    def restore_db_cluster_from_snapshot(self,*kwargs):
        client = boto3.client('rds')
        response = client.restore_db_cluster_from_snapshot(
            DBClusterIdentifier=kwargs[0],
            SnapshotIdentifier=kwargs[1],
            DBSubnetGroupName=kwargs[2],
            VpcSecurityGroupIds=[
                kwargs[3],
            ],
            Engine=kwargs[4],
	    EngineVersion=kwargs[5]	
        )
        print(response)

class RDSShare:
    def share_db_snapshot(self, snpshotName,accountName):
        client = boto3.client('rds')
        response = client.modify_db_snapshot_attribute(
            DBSnapshotIdentifier=snpshotName,
            #AttributeName='copy',
            AttributeName='restore',
            ValuesToAdd=[accountName]
            )
        print(response)

    def share_encrypted_db_snapshot(self, snpshotName,accountName):
        client = boto3.client('rds')
        response = client.modify_db_snapshot_attribute(
            DBSnapshotIdentifier=snpshotName,
            AttributeName='restore',
            ValuesToAdd=[accountName]
        )
        print(response)

class RDSStop:
    def stop_db_instance(self, *kwargs):
        client = boto3.client('rds')
        response = client.stop_db_instance(
            DBInstanceIdentifier=kwargs[0]
            #DBSnapshotIdentifier=kwargs[0],
        )
        print(response)

class RDSStart:
    def start_db_instance(self, *kwargs):
        client = boto3.client('rds')
        response = client.start_db_instance(
            DBInstanceIdentifier=kwargs[0]
        )
        print(response)

