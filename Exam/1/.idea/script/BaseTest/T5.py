#!/usr/bin/python
# -*- coding: GBK -*-
import os
import sys
#info=os.getcwd()
#listfile=os.listdir(os.getcwd())
info=input("������Ҫ�о��ļ���Ŀ¼��(��D:\\temp)")
listfile=os.listdir(info)
#out=open(listfile,'r')

for line in listfile:  #��Ŀ¼�µ��ļ�����ֵ��line�������
    print(line)         #��ӡ����ֵ������