#!/usr/bin/env python
#!-*- encoding=utf-8 -*-
#Auther: ZJ
#from __future__ import unicode_literals
import sys
import pexpect

child = pexpect.spawnu('ftp 49.234.17.164 4449')
child.expect('(?i)name .*:')
child.sendline('nginx')
child.expect('(?i)password:')
child.sendline('ftpuser')
child.expect('ftp>')
child.sendline('bin')
child.expect('ftp>')
child.sendline('cd web4')
child.expect('ftp>')
child.sendline('put login_act109.jpg')
child.expect('ftp>')
sys.stdout.write(child.before)
print("Escape character is '^]'.\n")
sys.stdout.write(child.after)
sys.stdout.flush
#child.interact()
child.sendline('quit')
child.close()
