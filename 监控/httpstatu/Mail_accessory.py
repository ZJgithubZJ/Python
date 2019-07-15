#!/usr/bin/env python3
#!-*- encoding=utf-8 -*-
#Auther:ZJ

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

class Sendmail:
	def __init__(self):
		self.sender = 'zhangjian@xnhd.com'
		self.receiver = 'zhangjian@xnhd.com'
		#创建实例
		self.message = MIMEMultipart()
		self.message['From'] = Header('Proxy_mail','utf-8')
		self.message['To'] = Header('ZJ','utf-8')
		self.message['Subject'] = Header('Python Test','utf-8')
		#邮件正文
		self.message.attach(MIMEText('Python 报警邮件测试，详情见附件','plain','utf-8'))
		#构造附件file1
		file1 = MIMEText(open('DERIV_CD.txt','r').read(),'base64','utf-8')
		file1['Content-Type'] = 'application/octet-stream'
		#filename为邮件中显示的名字，不必与真实文件名相同
		file1['Content-Disposition'] = 'attachment; filename = "file1.txt"'
		self.message.attach(file1)
		#构造附件att2，规则同上
		

	def sendmail(self):
		try:
			server = smtplib.SMTP_SSL('smtp.exmail.qq.com',465)
			server.login('zhangjian@xnhd.com','mail passwd')
			server.sendmail(self.sender,self.receiver,self.message.as_string())
			print('Mail send succeed!')
			server.quit()
		except Exception as e:
			print('Mail send failed', e)
if __name__ == '__main__':
	test = Sendmail()
	test.sendmail()	
