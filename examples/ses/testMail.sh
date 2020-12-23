#!/bin/bash
#Author: Sudheer Kondla, Sudheer.Kondla@IBM.com, Date: Feb 2, 2017
#Purpose: test/use email service SES 

SES_DIR=/home/admin/jobs/ses/emailList
DATETIME=`date`

sendEmail() {
    subject=${1}
    message=${2}
    /usr/bin/python3 -c \
     "from sesAdmin import sendEmail; sendEmail('$subject','$message')"
}

sendRawEmail() {
    fileName=${1}
    subject=${2}
    message=${3}
    echo "message: ${message}"  
    /usr/bin/python3 -c \
     "from sesAdmin import sendRawEmail; sendRawEmail('$fileName','$subject','$message')"
}

sendEmail "Test from `hostname -i` @$DATETIME" "Test from `hostname -i` @$DATETIME"
sendRawEmail test.json "Test from `hostname -i` @$DATETIME" "Test from `hostname -i` @$DATETIME" 


