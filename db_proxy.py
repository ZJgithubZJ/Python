#!/bin/bash/env python
#!-*- encoding=utf-8 -*-
import os
import sys
import MySQLdb
import db_engine
from db_engine import MysqlEngine
from  datetime import *
#from pymysql import connect
db = MysqlEngine(user='root',passwd='51..dmz',host='10.66.108.44',port=3306)

def ConnectAll():
	db.connect()
def DisconnectAll():
	db.disconnect()
	
def item(startdate,enddate):
	one_day = timedelta(days=1)
	allresult = []
	real_enddate = enddate + one_day
	while(startdate != real_enddate):
		sql_as_role = "select RoleID,ZoneID,count(*) from dmz_bill_%s.webtreasurebox group by zoneid,roleid;"
		real_sql = sql_as_role%(startdate.strftime('%Y%m%d'))
		print(real_sql)
		db.query(real_sql)
		result = db.fetch_result()
		allresult += list(result)
		startdate = startdate + one_day
	with open('webtreasurebox.xls','w') as f:
		for lines in allresult:
			if lines[2] > 10:
				f.write(str(lines[0])+'\t'+str(lines[1])+'\t'+str(lines[2])+'\t'+'\n')

def WeddingSum(startdate,enddate):
	one_day = timedelta(days = 1)
	allresult = []
	real_enddate = enddate + one_day
	while(startdate != real_enddate):
		sql_as_role = "select a.RoleID,a.ZoneID,loverid,ValueReq from dmz_bill_%s.money as a left join dmz_bill_%s.balance as b on a.roleid = b.roleid and a.zoneid = b.zoneid where a.ChannelID = 0x08030101 and b.loverid<>-1  group by a.roleid,a.zoneid"
		real_sql = sql_as_role%(startdate.strftime('%Y%m%d'),startdate.strftime('%Y%m%d'))
		print(real_sql)
		db.query(real_sql)
		result = db.fetch_result()
		allresult += list(result)
		startdate = startdate + one_day
	with open('weddingsum.xls','w') as f:
		for lines in allresult:
			f.write(str(lines[0])+'\t'+str(lines[1])+'\t'+str(lines[2])+'\t'+str(-int(lines[3]))+'\n')	
