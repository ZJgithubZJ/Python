#!/bin/bash/env python
#!-*- encoding=utf-8 -*-
#Auther: ZJ

from db_proxy import *
import sys

if __name__ == '__main__':
	ConnectAll()
	#item(date(2019,6,10), date(2019,6,11))
	WeddingSum(date(2019,6,20), date(2019,6,23))
	DisconnectAll()
