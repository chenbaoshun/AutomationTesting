#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : Base_Req.py
# @Author  : Baoshun.Chin
# @Time    : 2020-10-18 17:53
# @Site    : 
# @version : V1.0

import requests

class Base_Reg(object):
    def __init__(self):
        self.ip = 'http://121.42.15.146:9090'
        self.headers = {'X-Requested-With': 'XMLHttpRequest'}

    def post_trmplate(self,url,data,session=requests.session()):
        url = self.ip + url
        resp = session.post(url=url,data=data,headers=self.headers)
        return resp

if __name__ == '__mian__':
    url = '/mtx/index.php?s=/index/user/login.html'
    data = {'accounts':'bull','pwd':'123456'}
    req = Base_Reg()
    res = req.post_trmplate(url,data)
    print(res.json())