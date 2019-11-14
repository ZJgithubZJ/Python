#!/usr/bin/env python3
#!-*- encoding=utf-8 -*-
#Auther: ZJ
import sys
import func.overlord.client as fc

remotefile = '/usr/lib/python2.6/site-packages/func/minion/modules/mymodule.py'
localfile = '/usr/lib/python2.7/site-packages/func/minion/modules/mymodule.py'
try:
	client = fc.Client("*")
	print(client.local.copyfile.send(localfile, remotefile))
except Exception as e:
	print(str(e))

print(client.command.run('/etc/init.d/funcd restart'))
