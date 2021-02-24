#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
# @File    : md5Test.py
# @Author  : CHIN
# @Time    : 2020-12-25 21:39

'''
对请求参数做ASCII码的排序
做url encode编码：name=coco&age=18&city=chengdu&work=tester
做MD5 --> sign
'''

from urllib import parse
import hashlib

dict1 = {'name':'coco','age':18,'city':'chengdu','work':'tester'}
# datas = {'name':'coco','age':18,'city':'chengdu','work':'tester','sign':'sign'}

# dict1 = dict(sorted(dict1.items(),key=lambda item:item[0]))

# from urllib import parse
#
# datas = parse.urlencode(dict1)
# print(datas)
#
# import hashlib
# md5 = hashlib.md5()
# md5.update(datas.encode('utf-8'))
# print(md5.hexdigest())

def getMd5(**kwargs):
	dict1 = dict(sorted(kwargs.items(), key=lambda item: item[0]))
	datas = parse.urlencode(dict1)
	md5 = hashlib.md5()
	md5.update(datas.encode('utf-8'))
	return md5.hexdigest()

print(getMd5())
