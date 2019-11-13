#!/usr/bin/env python
#!-*- encoding=utf-8 -*-
#Auther: ZJ
from fabric import *

def put_task(c):
	try:
		if c.run('test -d /root/test', warn=True).failed:
			c.run('mkdir -p /root/test')
			c.put('/root/test/test.tgz','/root/test/test.tgz')
			print('Put task running ok!')
		else:
			c.put('/root/test/test.tgz','/root/test/test.tgz')
			print('Put task running ok!')
	except Exception as e:
		print(str(e))
def untar_task(c):
	try:
		result = c.run('cd /root/test && tar -zxvf test.tgz', hide=True)
		if result.ok:
			print('untar done!')
			c.run('/bin/bash /root/test/test.sh')
	except Exception as e:
		print(str(e))
@task
def color(c):
	print yellow('lalala')

@task
def all_task(c):
	put_task(c)
	untar_task(c)
