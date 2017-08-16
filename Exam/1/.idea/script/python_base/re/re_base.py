#!/usr/bin/python
# -*- coding: GBK -*-
import urllib.request
from lxml import etree
import re
request2 = "http://book.zongheng.com/chapter/189169/3431546.html";
response2 = urllib.request.urlopen(request2)
html= response2.read();
codeOfHtml=html.decode('utf-8')
page = etree.HTML(codeOfHtml.lower())
hrefs = page.xpath(u"//a")
print("-------------href.attrib-------------")
for href in hrefs:
    print(href.attrib)
print("--------------href.text------------")
for href in hrefs:
    print(str(href.text))
print("--------------re------------")
pattern = re.compile(r'(.*?)雪(.*)中(.*?).*',re.S|re.I)
#pattern = re.compile(r'(.*?)0(.*)7(.*?).*',re.S|re.I)
#pattern = re.compile(r'(.*?)0(.*)7(.*?).*')
#pattern = re.compile(r'(.*)0(.*)7(.*?).*')
#pattern = re.compile(r'(.*)0(.*)7(.*?)')
#pattern = re.compile(r'(.*)0(.*)7(.*)')
#pattern = re.compile(r'(.*)0(.*)7(.*)',re.S)
for href in hrefs:
    ss= str(href.text);
    match = pattern.match(ss)
    if match:
        print(match.group())