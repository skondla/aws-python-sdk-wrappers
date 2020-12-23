#!/bin/bash
# Author: Sudheer Kondla, 03/20/19, skondla@me.com
# Purpose: Scale DB instance(s) of specific environment

if [ $# -lt 2 ];
then
    echo "USAGE: bash $0 {instanceClass Environment}"
    exit 1
fi

instanceClass=$1
environ=$2
LOGDIR=/data2/output/snapshots

echo "instanceClass:$instanceClass"
#echo "environ: $3"

TODAY=`date '+%Y%m%d%H%M'`
echo "TODAY: $TODAY"

describeCluster() {
	dbClusterName=$1
	/usr/local/bin/aws rds describe-db-cluster-snapshots \
 	 | egrep '(DBClusterSnapshotArn|KmsKeyId)' \
 	 | grep "rds:$dbClusterName" | awk '{print $2}' |tail -1 | cut -f2 -d'"'
}

describeDBInstances() {
 dbEnv=$1	
 echo "dbEnv: $dbEnv"
 /usr/bin/python -c \
  "from rdsAdmin import RDSDescribe;rdsDesc=RDSDescribe();rdsDesc.rds_desc_db_instances_all()" \
  | /usr/local/bin/js-beautify | grep Address | awk '{print $3}' | cut -f1 -d"." | cut -f2 -d"'" |  grep "\-$dbEnv" \
  > $LOGDIR/scaledbInstances.txt

}

scaleDBInstance(){
 dbInstanceName=$1
 instanceClass=$2
 /usr/bin/python -c \
  "from rdsAdmin import RDSModify;rdsMod=RDSModify();rdsMod.modify_db_instance_class('$dbInstanceName','$instanceClass')" \
  > $LOGDIR/${dbInstanceName}.${instanceClass}.json
}

cd /home/admin/jobs/new

#sourceSnap=`describeCluster $clusterName`
#targetSnap=$clusterName-snapshot-$TODAY
echo "^^^^^^^^^^"

describeDBInstances $environ

for dbInst in `cat $LOGDIR/scaledbInstances.txt`
do
   scaleDBInstance $dbInst $instanceClass
done
