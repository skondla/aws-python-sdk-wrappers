#!/bin/bash
# Author: Sudheer Kondla, 03/20/19, skondla@me.com
# Purpose: Start DB instance(s) of specific environment

if [ $# -lt 1 ];
then
    echo "USAGE: bash $0 {Environment}"
    exit 1
fi

environ=$1
LOGDIR=/data2/output/snapshots

TODAY=`date '+%Y%m%d%H%M'`
echo "TODAY: $TODAY"

describeDBInstances() {
 dbEnv=$1	
 echo "dbEnv: $dbEnv"
 /usr/bin/python -c \
  "from rdsAdmin import RDSDescribe;rdsDesc=RDSDescribe();rdsDesc.rds_desc_db_instances_all()" \
  | /usr/local/bin/js-beautify | grep Address | awk '{print $3}' | cut -f1 -d"." | cut -f2 -d"'" |  grep "\-$dbEnv" \
  > $LOGDIR/scaledbInstances.txt

}

startDBInstance(){
 dbInstanceName=$1
 /usr/bin/python -c \
  "from rdsAdmin import RDSStart;;RDSStart().start_db_instance('$dbInstanceName')" \
  > $LOGDIR/${dbInstanceName}.start.json
}

cd /home/admin/jobs/new

#sourceSnap=`describeCluster $clusterName`
#targetSnap=$clusterName-snapshot-$TODAY
echo "^^^^^^^^^^"

describeDBInstances $environ

for dbInst in `cat $LOGDIR/scaledbInstances.txt`
do
   startDBInstance $dbInst
done
