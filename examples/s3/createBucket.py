
#!/usr/bin/env python3
#Author: skondla@me.com
#purpose: create S3 bucket in a given region, apply policy and eccrypt bucket
# -*- coding: utf-8 -*-

import sys
from s3Admin import CreateS3, UploadS3, CheckS3,EncryptS3

def checkBucket(bucketName,region):
    bucketStatus = CheckS3().check_bucket(bucketName)
    if bucketStatus:
        print("Bucket: " + bucketName + " exists, Don't create")
    else:
        if 'us-east-1' in region:
            CreateS3().createBucketUS(bucketName)
            CreateS3().createBucketPolicy(bucketName)
            EncryptS3().encryptBucket(bucketName)
        else:
            CreateS3().createBucket(bucketName,region)
            CreateS3().createBucketPolicy(bucketName)
            EncryptS3().encryptBucket(bucketName)

def uploadToS3Bucket():
    pass

if __name__ == "__main__":
    if len(sys.argv) < 3:
        """ Enter Arguments """
        print('Please Enter S3 Bucket Name and Region.  \n !!!Exiting !!!')
        exit()
    else:
        bucketName = sys.argv[1]
        region = sys.argv[2]
        checkBucket(bucketName,region)
