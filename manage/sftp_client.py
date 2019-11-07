#!/usr/bin/env python
#!-*- encoding=utf-8 -*-
#Auther: ZJ
import paramiko
import sys

username = 'root'
hostname = '10.105.70.21'
port = 22
password = ''

try:
  t = paramiko.Transport((hostname,port))
  t.connect(username=username,password=password)				#这里好像只能使用密码方式，没有秘钥方式
  sftp = paramiko.SFTPClient.from_transport(t)
  sftp.put("/root/test/syslogin.log","/root/syslogin.log")			#要具体到目标端的文件名
  sftp.get("/root/www.xx5.com.20190315.tgz","/root/www.xx5.com.20190315.tgz")	#要具体到本地端的文件名
  sftp.mkdir("/root/test",755)			#这是是三位数的权限，不能是0755，被坑了！
  t.close()
except Exception as e:
  print(str(e))
