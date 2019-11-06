#!/usr/bin/env python
#!-*- encoding=utf-8 -*-
#Auther: ZJ
'''
功能：实现通过秘钥登录多台机器执行指令
此脚本要求本机要能够与iplist.txt里的所有主机无秘钥通信
此处iplist.txt文件未列出
'''
import paramiko
import sys

username = 'root'
port = 22
ssh = paramiko.SSHClient()		#创建ssh客户端对象
key = paramiko.AutoAddPolicy()		#自动添加主机名以及秘钥到本地HostKey对象，不依赖load_system_host_keys()
ssh.set_missing_host_key_policy(key)	#设置远程主机没有本地主机的秘钥或HostKey对象时的策略
pkey = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')	#指定私钥文件

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
