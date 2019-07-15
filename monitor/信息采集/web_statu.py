#!/usr/bin/env python3
#!-*- encoding=utf-8 -*-
#Auther:ZJ

import os,sys
import time
import pycurl

URL = "http://www.baidu.com"
c = pycurl.Curl()
c.setopt(pycurl.URL,URL)
c.setopt(pycurl.CONNECTTIMEOUT, 5)
#c.setopt(pycurl.TIMEOUT, 120)
c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)
indexfile = open('/root/test/indexfile.txt', 'wb')
c.setopt(pycurl.WRITEHEADER, indexfile)
c.setopt(pycurl.WRITEDATA, indexfile)
try:
	c.perform()
except Exception as e:
	print('Connect error:', e)
	indexfile.close()
	c.close()
	sys.exit()

NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
HTTP_CODE = c.getinfo(c.HTTP_CODE)
SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)

print('Target url: {}'.format(URL))
print('HTTP状态码: {}'.format(HTTP_CODE))
print('DNS解析时间: {:.2f} ms'.format(NAMELOOKUP_TIME*1000))
print('建立链接时间: {:.2f} ms'.format(CONNECT_TIME*1000))
print('准备传输时间: {:.2f} ms'.format(PRETRANSFER_TIME*1000))
print('传输开始时间: {:.2f} ms'.format(STARTTRANSFER_TIME*1000))
print('传输结束总时间: {:.2f} ms'.format(TOTAL_TIME*1000))
print('下载数据包大小: {:.2f} MB'.format(SIZE_DOWNLOAD/(1024*1024)))
print('HTTP头部大小：{} byte'.format(HEADER_SIZE))
print('平均下载速度: {:.2f} kB/s'.format(SPEED_DOWNLOAD/1024))
indexfile.close()
c.close()
