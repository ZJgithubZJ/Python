#!/usr/bin/env python
#!-*- encoding=utf-8 -*-
#Auther: ZJ
'''
随机生成14位随机密码，其中包括大小写字母、数字以及标点符号。
'''
import random,string
num_passwd = input('请输入你想要生成的密码条数：')
password = []
for i in range(int(num_passwd)):
	password = random.sample(string.ascii_lowercase, 2)
	password.extend(random.sample(string.ascii_uppercase,2))
	password.extend(random.sample(string.punctuation, 2))
	password.extend(random.sample(string.digits, 2))
	password.extend(random.sample(string.ascii_letters,6))
	random.shuffle(password)
	#print(password)
	final_password = ''.join(password)
	print(final_password)
