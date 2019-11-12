#!/usr/bin/env python
#!-*- encoding=utf-8 -*-
#Auther: ZJ
import paramiko
import sys

username = 'root'
hostname = '10.105.70.21'
port = 22
password = '51..dmz'

try:
  t = paramiko.Transport((hostname,port))
  t.connect(username=username,password=password)
  sftp = paramiko.SFTPClient.from_transport(t)
  sftp.put("/root/test/syslogin.log","/root/syslogin.log")
  sftp.get("/root/www.xx5.com.20190315.tgz","/root/www.xx5.com.20190315.tgz")
  sftp.mkdir("/root/test",755)
  t.close()
except Exception as e:
  print(str(e))
