#!/bin/bash/env python
#!-*- encoding=utf-8 -*-
#Auther: ZJ
import os
def FB(path):
        for filepath,dirs,files in os.walk(path):
                for f in files:
                        pfile = os.path.join(filepath,f)
                        fsize = os.path.getsize(pfile)
                        fsize = round(float(fsize / (1024*1024)),2)
                        if fsize > 20:
                                print('Big File: ' + str(pfile) + ' ' + str(fsize) + 'MB')
if __name__ == '__main__':
        path = '/root/test'
        FB(path)
