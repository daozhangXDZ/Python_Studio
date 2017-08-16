#!/usr/bin/python
# -*- coding: GBK -*-
import os
import urllib.request
import re

catchwebresult = "catchwebresult";

def getHtml(url):
    #print("���ڴ���ҳ����ȡ....")
    page=urllib.request.urlopen(url)
    Html=str(page.read())
    print("�ɹ���ȡ....")
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
        print("���ͼƬ����......");
        return;

    print("img_list[0]=", img_list[0])
    print("��������ͼƬ......")

    for i in range(len(img_list)):
        print("img_list[%d]=%s" % (i,img_list[i]))
        urllib.request.urlretrieve(img_list[i],catchwebresult+"/"+pSavePath+'/NO/%s.jpg' % (i),Schedule)
    print("���ͼƬ����......")
    print("һ��ץ����%d��ͼƬ" % len(img_list))

if __name__=="__main__":
    # '''"http://tieba.baidu.com/f?kw=%B0%A2%C9%AD%C4%C9"'''
    vPatchURL= input();
    vSavePath = input();
    html=getHtml(vPatchURL);
    getImgNormal(html,vSavePath)
    #getImgBaidu(html, vSavePath)