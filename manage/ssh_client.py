#!/usr/bin/env python
#!-*- encoding=utf-8 -*-
#Auther: ZJ
'''
此脚本要求本机要能够与iplist.txt里的所有主机无秘钥通信
此处iplist.txt文件未列出
'''
import paramiko
import sys

username = 'root'
port = 22
ssh = paramiko.SSHClient()		#创建ssh客户端对象
key = paramiko.AutoAddPolicy()		#自动添加主机名以及秘钥到本地HostKey对象，不依赖load_system_host_keys()
ssh.set_missing_host_key_policy(key)	#设置
pkey = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')

def run():
  for ip in open('iplist.txt', 'r'):
    print("------------ split line ------------")
    print(ip)
    try:
      ssh.connect(ip,port,username,pkey,timeout=5)    
      stdin,stdout,stderr = ssh.exec_command('free -m')
      for line in stdout.readlines():
        print(line)
        ssh.close()
    except Exception as e:
      print(ip + str(e))
  return

if __name__ == '__main__':
  run()
