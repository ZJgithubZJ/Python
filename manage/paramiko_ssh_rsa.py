#!/usr/bin/env python
#!-*- encoding=utf-8 -*-
#Auther: ZJ
import paramiko
import sys

username = 'root'
port = 22
ssh = paramiko.SSHClient()
key = paramiko.AutoAddPolicy()
ssh.set_missing_host_key_policy(key)
pkey = paramiko.RSAKey.from_private_key_file('/root/test/private.key') #/root/.ssh/id_rsa是默认位置，可以放到别处

def run():
  with open('iplist.txt', 'r') as f:
    for line in f.readlines():
      print("------------ split line ------------")
      ip = line.split()[1]
      print(line)
      try:
        ssh.connect(ip,port,username,pkey)    
        stdin,stdout,stderr = ssh.exec_command('free -m')
        for result in stdout.readlines():
          print(result.strip())
          ssh.close()
      except Exception as e:
        print(ip + str(e))
  return

if __name__ == '__main__':
  run()
