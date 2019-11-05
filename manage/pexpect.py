#!/usr/bin/env python
#!-*- encoding=utf-8 -*-
#Auther: ZJ
#from __future__ import unicode_literals	#这里不知道为什么要用unicode编码
import sys
import pexpect

child = pexpect.spawnu('ftp 49.234.17.164 4449')
child.expect('(?i)name .*:')			#(?i)表示忽略大小写匹配
child.sendline('nginx')
child.expect('(?i)password:')
child.sendline('ftpuser')
child.expect('ftp>')
child.sendline('bin')
child.expect('ftp>')
child.sendline('cd web4')
child.expect('ftp>')
child.sendline('put login_act109.jpg')		#定义操作
child.expect('ftp>')
sys.stdout.write(child.before)			#打印最近一次匹配成功之前的内容
print("Escape character is '^]'.\n")
sys.stdout.write(child.after)			
sys.stdout.flush				#刷新sys.stdout，在屏幕上看到实时输出
#child.interact()				#让出控制权，退出脚本，进入到交互式界面
child.sendline('quit')
child.close()
