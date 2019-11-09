#!/usr/bin/env python
#!-*- encoding=utf-8 -*-
#Auther: ZJ
'''
单台服务器的无秘钥连接执行指令方式
'''
#from fabric import Connection
#c = Connection('10.105.70.21',port=22,user='root')
#result = c.run('uname -a')
#if result.ok:
#  print('Connection is ok')
#print(result.connection.host)

'''
单台服务器的秘钥连接执行指令方式
'''
#from fabric import Connection
#c = Connection(
#	host = '10.105.70.21',
#	user = 'root',
#	port = 22,
#	connect_kwargs={
#		"key_filename": "/root/test/private.key"
#	}
#)
#result = c.run('uname -a')
#if result.ok:
# 	print('Connection is ok')
#print(result.connection.host)

'''
单台服务器的sudo用户密码执行指令方式
'''
#from invoke import Responder
#from fabric import Connection
#c = Connection('10.105.70.21')
#sudopass = Responder(			#Responder是用来自动输入密码，不用手动type了，但一般sudo用户都不需要输入密码的
#	pattern = r'\[sudo\] password:',
#	response = 'mypassword\n',
#)
#c.run('sudo whoani', ppty=True, watchers=[sudopass])

'''
单台服务器的上传文件代码以及解压指令
'''
#from fabric import Connection
#c = Connection('10.105.70.21')
#c.put("/root/test/test.tgz","/root/test/test.tgz")
#result = c.run('cd /root/test && tar -zxvf test.tgz')
#if result.ok:
#  print("Upload and unpack secceed")
#else:
#  print("something error")

'''
多台主机执行指令，主机ip逐行写入iplist.txt文件
'''
#from fabric import Connection
#with open('iplist.txt', 'r') as f:
#  lines = f.readlines()
#  for ip in lines:
#    try:								#使用try捕捉异常，使得即使中间出现异常主机依旧能够输出错误并继续循环
#      result = Connection(ip).run('uname -a')
#      print("{}: {}".format(ip.strip(),result.stdout.split()[0]))	#ip.strip()是规避输出'\n'，出现多余空格
#    except Exception as e:
#      print(ip.strip()+" "+str(e))

'''
多台主机执行多条指令
'''
#from fabric import Connection
#with open('iplist.txt','r') as f:
#  for ip in f.readlines():
#    try:
#      c = Connection(ip)
#      if c.run('test -d /root/test', warn=True).failed:			#先判断目标路径是否存在
#        c.run('mkdir -p /root/test')
#        c.put('/root/test/test.tgz','/root/test/')
#        c.run('cd /root/test && tar -zxvf test.tgz',hide=True)		#hide=True表示隐藏指令的输出结果，否则都是解压的指令输出，很乱！
#        print(ip.strip()+" "+"done!")
#      else:
#        c.put('/root/test/test.tgz','/root/test/')
#        c.run('cd /root/test && tar -zxvf test.tgz',hide=True)
#        print(ip.strip()+" "+"done!")
#    except Exception as e:
#      print(ip.strip()+" "+str(e))
