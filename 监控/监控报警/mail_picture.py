#!/usr/bin/env python3
#!-*- encoding=utf-8 -*-
#Auther:ZJ

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header

class Sendmail:
	def __init__(self):
		self.sender = 'zhangjian@xnhd.com'
		self.receiver = 'zhangjian@xnhd.com'
		#创建实例
		self.msgroot = MIMEMultipart('related')
		self.msgroot['From'] = Header('ZJ','utf-8')
		self.msgroot['To'] = Header('ZJ','utf-8')
		self.msgroot['Subject'] = Header('Python Test','utf-8')
		self.msgAlternative = MIMEMultipart('alternative')
		self.msgroot.attach(self.msgAlternative)
		#邮件正文
		self.mail_msg =	"""
		<p>图片邮件测试</p>
		<p>系统监控详情:</p>
		<p><img src="cid:image1.png"></p>
		<p><img src="cid:image2.png"></p>
		<p><img src="cid:image3.png"></p>
		<p><img src="cid:image4.png"></p>
		"""
		self.msgAlternative.attach(MIMEText(self.mail_msg,'html','utf-8'))
		self.mg1 = open('image1.png','rb')
		self.msgImage = MIMEImage(self.mg1.read())
		self.mg1.close()
		self.msgImage.add_header('Content-ID','<image1.png>')
		self.msgroot.attach(self.msgImage)
		self.mg2 = open('image2.png','rb')
		self.msgImage = MIMEImage(self.mg2.read())
		self.mg2.close()
		self.msgImage.add_header('Content-ID','<image2.png>')
		self.msgroot.attach(self.msgImage)
		self.mg3 = open('image3.png','rb')
		self.msgImage = MIMEImage(self.mg3.read())
		self.mg3.close()
		self.msgImage.add_header('Content-ID','<image3.png>')
		self.msgroot.attach(self.msgImage)
		self.mg4 = open('image4.png','rb')
		self.msgImage = MIMEImage(self.mg4.read())
		self.mg4.close()
		self.msgImage.add_header('Content-ID','<image4.png>')
		self.msgroot.attach(self.msgImage)

	def sendmail(self):
		try:
			server = smtplib.SMTP_SSL('smtp.exmail.qq.com',465)
			server.login('zhangjian@xnhd.com','mail passwd')
			server.sendmail(self.sender,self.receiver,self.msgroot.as_string())
			print('Mail send succeed!')
			server.quit()
		except Exception as e:
			print('Mail send failed', e)
if __name__ == '__main__':
	test = Sendmail()
	test.sendmail()	
