#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_fzcases_13.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-10 10:08
# @Site    : 
# @version : V1.0

'''
请求方法：
请求地址：
方法，地址，**kwargs
'''

import requests

class Methods:
    def get(self, url, **kwargs):
        try:
            return requests.get(url=url, **kwargs)
        except BaseException as e:
            return e.args[0]
        # except:
        #     raise '接口请求参数错误'

    def post(self, url, **kwargs):
        try:
            return requests.post(url=url, **kwargs)
        except BaseException as e:
            return e.args[0]

obj = Methods()
# g = obj.get(url='http://www.baidu.com/')
g = obj.get(url='http://www.123343545.org')
print(g.status_code)
print(g.text)

p = obj.post(url='')
print(p.status_code)
print(p.text)

'''第2种封装思路'''
class Requests:
    def request(self, url, method='get', **kwargs):
        return requests.request(url=url, method=method, **kwargs)