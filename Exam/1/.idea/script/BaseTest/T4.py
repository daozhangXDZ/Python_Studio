#!/usr/bin/python
# -*- coding: GBK -*-

# ��һ���ļ�
fo = open("foo.txt", "r+")
str = fo.read(10);
print("��ȡ���ַ����� : ", str)

# ���ҵ�ǰλ��
position = fo.tell();
print("��ǰ�ļ�λ�� : ", position)

# ��ָ���ٴ����¶�λ���ļ���ͷ
position = fo.seek(0, 0);
str = fo.read(10);
print("���¶�ȡ�ַ��� : ", str)
# �رմ򿪵��ļ�
fo.close()