#!/usr/bin/env python
# -*- encoding=utf-8 -*-
#Auther: ZJ
import sys
from sys import argv
import difflib

try:
	file1 = argv[1]
	file2 = argv[2]
except Exception as e:
	print('Error: '+str(e))
	print('Usage: diff.py file1 file2')
	sys.exit()

def readline(filename):
	with open(filename, 'r') as f:
		return f.readlines()

line1 = readline(file1)
line2 = readline(file2)
d = difflib.HtmlDiff()
print(d.make_file(line1, line2))
