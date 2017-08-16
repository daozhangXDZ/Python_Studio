#!/usr/bin/python
# -*- coding: GBK -*-
import urllib.request;
import urllib.response;
values = {"username": "1016903103@qq.com", "password": "XXXX"}
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
response = urllib.request.urlopen(url);
print(response.read());