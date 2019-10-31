#!/usr/bin/env python
#!-*- encoding=utf-8 -*-
#Auther:ZJ
'''
客户端：
1:yum install -y clamd clamav clamav-update
2:chkconfig clamd on
3:/usr/bin/freshclam
4:setenforce 0
5:sed -i -e '/^TCPAddr/ s/127.0.0.1/0.0.0.0/' /etc/clamd.conf
6:/etc/init.d/clamd start

主控端:
1:wget http://xael.org/norman/python/pyclamd/pyClamd-0.3.15.tar.gz
2:tar -zxvf pyClamd-0.3.15.tar.gz
3:cd pyClamd-0.3.15
4:python setup.py install
'''

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
        print(self.ip+" "+"connection ok...")
      else:
        print(self.ip+" "+"connection error...")
        return
      cd.reload()
      '''
      若检测对象为多个，可使用multiscan_file多线程扫描方法
      print(cd.multiscan_file(self.path))
      '''
      print(cd.contscan_file(self.path))
    except Exception as e:
      print(self.ip+" "+str(e))

IPs = ['10.105.70.21']
port = 3310
path = '/app/nginx/wwwroot/xx5/www.xx5.com/wwwroot/bbs/attachments'
#path = '/tmp'
for ip in IPs:
  currp = scan(ip,port,path)
  currp.run()
