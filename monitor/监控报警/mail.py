#!/usr/bin/env python3
#!-*- encoding=utf-8 -*-
#Auther:ZJ

import smtplib
from email.mime.text import MIMEText
from email.header import Header

class Sendmail:
	def __init__(self):
		#真实发信人
		self.sender = 'mail01'
		#真实收信人
		self.receiver = 'zhangjian@xnhd.com'
		self.message = MIMEText('Python mail01.storyawine 测试邮件','plain','utf-8')
		#self.message = message
		#账面显示的From、To，真实是由self.sender代发。
		self.message['From'] = Header('75-65','utf-8')
		self.message['To'] = Header('zhangjian','utf-8')
		self.message['Subject'] = Header('Python SMTP test','utf-8')
	def sendmail(self):
		try:
			server = smtplib.SMTP('mail01.storyawine.com')
			#server.login('zhangjian@xnhd.com','mail passwd')
			server.sendmail(self.sender,self.receiver,self.message.as_string())
			print('Mail send succeed!')
			server.quit()
		except Exception as e:
			print('Mail send failed', e)
if __name__ == '__main__':
	test = Sendmail()
	test.sendmail()
