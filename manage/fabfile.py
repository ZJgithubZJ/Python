#!/usr/bin/env python
#!-*- encoding=utf-8 -*-
#Auther: ZJ
from fabric import *

@task
def webtask(c):
	try:
		c.run('df -h')
	except Exception as e:
		print(str(e))
@task
def dbtask(c):
	try:
		c.run('free -m')
	except Exception as e:
		print(str(e))

@task
def all(c):
	webtask(c)
	dbtask(c)
