#!/usr/bin/env python
#!-*- encoding=utf-8 -*-
#Auther: ZJ
import paramiko
import sys

username = 'root'
port = 22
password = '51..dmz'
ssh = paramiko.SSHClient()
key = paramiko.AutoAddPolicy()
ssh.set_missing_host_key_policy(key)

def run():
  with open('iplist.txt', 'r') as f:
    for line in f.readlines():
      print("------------ split line ------------")
      ip = line.split()[1]
      print(line)
      try:
        ssh.connect(hostname=ip,port=port,username=username,password=password)
        stdin,stdout,stderr = ssh.exec_command('free -m')
        for result in stdout.readlines():
          print(result.strip())
          ssh.close()
      except Exception as e:
        print(ip + str(e))
  return

if __name__ == '__main__':
  run()
