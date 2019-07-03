#!/usr/bin/env python
#!-*- encoding=utf-8 -*-

import dns.resolver
import os
import http
import http.client
import logging
import socket
from alarm import monitor

iplist = []
appdomain = 'app7.wsdo.xnhdgame.com'

def get_iplist(domain):
	try:
		A = dns.resolver.query(domain, 'A')
	except:
		logging.error('dns resolver error on get_iplist ')
		return
	for i in A.response.answer:
		for j in i.items:
			iplist.append(j.address)
			#print(j)
	return True

def checkip(ip):
	checkurl = ip
	socket.setdefaulttimeout(5)
	conn = http.client.HTTPConnection(checkurl, 80)
	getcontext = ""
	#print(conn)
	
	try:
		conn.request("GET","/watch.html",headers = {"Host": appdomain})
		r = conn.getresponse()
		getcontext = str(r.read())
	finally:
		if getcontext == "b'200\\n'":
			print(ip,"ok")
		else:
			A = monitor('domain: '+appdomain+' : '+ip+' is down,please check quickly')
			A.monitor_send()
			print(ip+' is down and alarm text has been sended to engineer!')

if __name__ == '__main__':
#	get_iplist(appdomain)
#	print(iplist)
	if get_iplist(appdomain) and len(iplist) > 0:
		for ip in iplist:
			checkip(ip)
	else:
		print("Dns resolve error on checkip!")
