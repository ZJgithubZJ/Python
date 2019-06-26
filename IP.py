#!/bin/bash/env python
#!-*- encoding=utf-8 -*-

from IPy import IP

ip_s = input('Please input an IP or net-range: ')
ips = IP(ip_s)

if len(ips) > 1:
        print('net: %s' % ips.net())                            #输出网络地址
        print('netmask: %s' % ips.netmask())                    #输出子网掩码
        print('broadcast: %s' % ips.broadcast())                #输出网络广播地址
        print('reverse address: %s' % ips.reverseNames()[0])    #输出地址反向解析
        print('subnet: %s' % len(ips))                          #输出子网的个数
else:                                                           #如果是单个IP的话
        print('reverse address: %s' % ips.reverseNames()[0])    #同上
        
print('hexadecimal: %s' % ips.strHex())                 #输出十六进制
print('binary: %s' % ips.strBin())                      #输出二进制
print('iptype: %s' % ips.iptype())                      #输出地址类型
