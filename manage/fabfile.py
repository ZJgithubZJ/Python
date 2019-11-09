#!/usr/bin/env python
#!-*- encoding=utf-8 -*-
#Auther: ZJ
from fabric import *

@task
def webtask(c):
	c.run('df -h')
@task
def dbtask(c):
	c.run('free -m')

@task
def all(c):
	webtask(c)
	dbtask(c)
