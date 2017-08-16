#!/usr/bin/python
# -*- coding: GBK -*-
import os
import sys
#info=os.getcwd()
#listfile=os.listdir(os.getcwd())
info=input("请输入要列举文件的目录：(如D:\\temp)")
listfile=os.listdir(info)
#out=open(listfile,'r')

for line in listfile:  #把目录下的文件都赋值给line这个参数
    print(line)         #打印出赋值的内容