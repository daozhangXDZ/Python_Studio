#!/usr/bin/python
# -*- coding: GBK -*-
import os
import urllib.request
import re

catchwebresult = "catchwebresult";

def getHtml(url):
    #print("正在打开网页并获取....")
    page=urllib.request.urlopen(url)
    Html=str(page.read())
    print("成功获取....")
    return Html

def Schedule(a,b,c):
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100;
    print('%.2f%%' % per);

def makerDir(pPath, isrelease):
    if isrelease:
        strPath = os.getcwd() + "/" + catchwebresult + "/" + pPath;
    else:
        strPath = pPath;
    if os.path.exists(strPath):
        return ;
    else:
        os.makedirs(strPath);

def getImgNormal(html,pSavePath):
    print("the type of html is :",type(html))
    img_re = re.compile(r'(?<=src=")\S+?jpg')
    # img_re=re.compile(r'src="(.*?\.jpg)"')
    img_list=img_re.findall(html)
    print("len(img_list)=",len(img_list))
    makerDir(pSavePath + "/NO", True);
    if( len(img_list) <= 0):
        print("完成图片下载......");
        return;

    print("img_list[0]=", img_list[0])
    print("正在下载图片......")

    for i in range(len(img_list)):
        print("img_list[%d]=%s" % (i,img_list[i]))
        urllib.request.urlretrieve(img_list[i],catchwebresult+"/"+pSavePath+'/NO/%s.jpg' % (i),Schedule)
    print("完成图片下载......")
    print("一共抓到了%d张图片" % len(img_list))

if __name__=="__main__":
    # '''"http://tieba.baidu.com/f?kw=%B0%A2%C9%AD%C4%C9"'''
    vPatchURL= input();
    vSavePath = input();
    html=getHtml(vPatchURL);
    getImgNormal(html,vSavePath)
    #getImgBaidu(html, vSavePath)