#!/usr/bin/env python3
#Author: skondla@me.com
#Purpose: Simple Email Service Administration
import os
import boto3
from botocore.exceptions import ClientError
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from boto.beanstalk import response
import json


def sesClient():
	ses = boto3.client('ses')
	return ses

def sendEmail(subject,content):
	# def sendEmail(subject,message):
	client = sesClient()
	#toAddr = emailList('email.to')
	toAddr = open(os.environ['SES_DIR']+'/recipients.list', 'r')
	toAddr = ' '.join(map(str, toAddr))
	ccAddr = open(os.environ['SES_DIR']+'/cc.list', 'r')
	ccAddr = ' '.join(map(str, ccAddr))
	bccAddr = open(os.environ['SES_DIR']+'/bcc.list', 'r')
	bccAddr = ' '.join(map(str, bccAddr))
	response = client.send_email(
		Destination={
			'BccAddresses':
				#bccAddr,
				bccAddr.split(','),
			'CcAddresses':
				#ccAddr,
				ccAddr.split(','),
			'ToAddresses':
				toAddr.split(',')
				#toAddr,
		},
		Message={
			'Body': {
				'Text': {
					'Charset': 'UTF-8',
					'Data': '%s' % content,
				},
			},
			'Subject': {
				'Charset': 'UTF-8',
				'Data': '%s' % subject,
			},
		},
		Source='sudheer.kondla@ibm.com',
		#SourceArn='arn:aws:ses:us-east-1:779129402617:identity/sudheer.kondla@ibm.com',
	)
	return response


# print(response)

def emailList(fileName):
	""" Pass email distribution file name(s)"""
	with open(fileName) as f:
		emailAddr = [line.rstrip() for line in f]
	# print('EMAILS: ', json.dumps(emailAddr))
	return emailAddr

def sendEmailAttach(fileName, content):
	client = sesClient()
	toAddr = emailList(os.environ['SES_DIR']+'/email.to')
	ccAddr = emailList(os.environ['SES_DIR']+'/email.cc')
	bccAddr = emailList(os.environ['SES_DIR']+'/email.bcc')
	message = MIMEMultipart()
	message['Subject'] = content[0]
	message['From'] = 'Sudheer.Kondla@ibm.com'
	message['To'] = ', '.join(toAddr)
	part = MIMEText(content[1], 'html')
	message.attach(part)
	# attachment
	if fileName:  # if bytestring available
		part = MIMEApplication(open(fileName, 'rb').read())
		part.add_header('Content-Disposition', 'attachment', filename=fileName)
		message.attach(part)

		response = client.send_raw_email(
			Destination={
				'BccAddresses':
					bccAddr,
				'CcAddresses':
					ccAddr,
				'ToAddresses':
					toAddr,
			},
			RawMessage={
				'Data': message.as_string()
			}
			# Source='sudheer.kondla@ibm.com',
			# SourceArn='arn:aws:ses:us-east-1:779129402617:identity/sudheer.kondla@ibm.com',
		)

	else:  # if file provided
		part = MIMEApplication(str.encode('attachment_string'))

	return response

def sendRawEmail(fileName,subject,content):
	toAddr = open(os.environ['SES_DIR']+'/recipients.list', 'r')
	toAddr = ' '.join(map(str, toAddr))
	print('content: ', content)
	SENDER = "sudheer.kondla@ibm.com"
	RECIPIENT = toAddr
	AWS_REGION = os.environ['AWS_REGION']
	SUBJECT = subject
	ATTACHMENT = "" + fileName + ""
	BODY_TEXT = content
	BODY_HTML = """\
    	<html>
    	<head></head>
    	<body>
    	<h1>Hello!</h1>
    	<p>{content}</p>
    	</body>
    	</html>
    	""".format(content=content)
	CHARSET = "utf-8"
	client = boto3.client('ses', region_name=AWS_REGION)
	msg = MIMEMultipart('mixed')
	msg['Subject'] = SUBJECT
	msg['From'] = SENDER
	msg['To'] = RECIPIENT
	msg_body = MIMEMultipart('alternative')
	textpart = MIMEText(BODY_TEXT.encode(CHARSET), 'plain', CHARSET)
	htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)
	msg_body.attach(textpart)
	msg_body.attach(htmlpart)
	att = MIMEApplication(open(ATTACHMENT, 'rb').read())
	att.add_header('Content-Disposition', 'attachment', filename=os.path.basename(ATTACHMENT))
	msg.attach(msg_body)
	msg.attach(att)
	try:
		# Provide the contents of the email.
		response = client.send_raw_email(
			Source=SENDER,
			Destinations=
			RECIPIENT.split(',')
			,
			RawMessage={
				'Data': msg.as_string(),
			},
		)
		Source = 'sudheer.kondla@ibm.com',
		SourceArn = 'arn:aws:ses:us-east-1:779129402617:identity/sudheer.kondla@ibm.com',
	except ClientError as e:
		print(e.response['Error']['Message'])
	else:
		print("Email sent! Message ID:"),
		print(response['MessageId'])
