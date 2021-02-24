#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
# @File    : postmanAi.py
# @Author  : CHIN
# @Time    : 2020-12-23 23:47

import json
import requests

class Requests:
	def request(self,method='get',url=None,**kwargs):
		if method=='get':
			requests.request(method='get',url=url,**kwargs)
		elif method=='post':
			requests.request(method='post', url=url, **kwargs)
		elif method=='put':
			requests.request(method='put', url=url, **kwargs)
		elif method=='delete':
			requests.request(method='delete', url=url, **kwargs)

def readJson():
	return json.load(open('api_test.json','r',encoding='utf-8'))

one = readJson()['item'][0]['request']
# print(one)

def one_get():
	r = requests.request(method=one['method'],url=one['url']['raw'])
	print(r.json())

one_get()