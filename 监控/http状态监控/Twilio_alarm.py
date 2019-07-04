#!/usr/bin/env python
#!-*- encoding=utf-8 -*-
"""免费套餐下，每个验证手机号每天只能接收5条信息"""
"""python3.7与最新版的twilio.6.28模块不兼容，需要安装twilio.5.8，坑了我很久"""
from twilio.rest import Client

class monitor:
	def __init__(self,text):
		self.text = text
	def monitor_send(self):
		self.account_sid = 'AC172c8186da0292f68ebe4e3dd270****'
		self.auth_token = '93eb0095f33c535f81582c63be21****'
		self.client = Client(self.account_sid, self.auth_token)
		message = self.client.messages.create(
			to='+86187****0391',
			#to='+86180****1811',
			body = self.text,
			from_='+12056199851'
		)
		#print(message.sid)

#if __name__ == '__main__':
#	A = monitor("test-5")
#	A.monitor_send()
