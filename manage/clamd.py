#!/usr/bin/env python
#!-*- encoding=utf-8 -*-
#Auther:ZJ
import pyclamd
class scan:
  def __init__(self,ip,port,path):
    self.ip = ip
    self.port = port
    self.path = path
  def run(self):
    cd = pyclamd.ClamdNetworkSocket(self.ip,self.port)
    try:
      if cd.ping():
        print('Connection OK...')
      else:
        print('Connection Error!')
        return
      cd.reload()
      print(cd.contscan_file(self.path))
    except Exception as e:
      print(self.ip + str(e))

IPs = ['10.105.70.21']
port = 3310
path = '/app/nginx/wwwroot/xx5/www.xx5.com/wwwroot/bbs/attachments'
#path = '/tmp'
for ip in IPs:
  currp = scan(ip,port,path)
  currp.run()
