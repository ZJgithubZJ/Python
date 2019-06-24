#!/bin/bash/env python
#!-*- encoding=utf-8 -*-
#Auther: ZJ

import os
import logging
import sys
import MySQLdb

class MysqlEngine:
        def __init__(self,user, passwd, host, port):
                self.user = user
                self.passwd = passwd
                self.host = host
                self.port = port
        def connect(self):
                try:
                        self.connection = MySQLdb.connect(user=self.user, passwd=self.passwd, host=self.host, port=self.port)
                        self.cursor = self.connection.cursor()
                        print('connect mysql succee!')
                except:
                        logging.error('connect mysql failed!')
                        sys.exit(0)
        def query(self,sql):
                try:
                        self.cursor.execute(sql)
                except:
                        logging.error('query failed!')
        def commit(self):
                self.connection.commit()
        def fetch_result(self):
                return self.cursor.fetchall()
        def disconnect(self):
                try:
                        self.cursor.close()
                        self.connection.close()
                        print('disconnected..')
                except:
                        logging.error('disconnect failed!')
