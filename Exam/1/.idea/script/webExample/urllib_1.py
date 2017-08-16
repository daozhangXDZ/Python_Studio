#!/usr/bin/python
# -*- coding: GBK -*-
import urllib.request
response1= urllib.request.urlopen("http://www.baidu.com");
strweb1= response1.read();
