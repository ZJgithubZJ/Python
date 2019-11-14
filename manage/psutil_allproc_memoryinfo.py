#!/usr/bin/env python3
#!-*- encoding=utf-8 -*-
#!Auther: ZJ
import os
import psutil
a = {}
for pid in psutil.pids():
	try:
		process = psutil.Process(pid)
		a[pid] = process.memory_info().rss
	except Exception as e:
		print(str(e))
#print(a)
for i in sorted(a,key=a.__getitem__):
	name = psutil.Process(i).name()
	path = psutil.Process(i).exe()
	print("{0:20}   {1:35}   {2:30}  {3:30}".format(name,path,i,a[i]))
