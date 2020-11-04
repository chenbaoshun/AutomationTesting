#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : Base_Req.py
# @Author  : Baoshun.Chin
# @Time    : 2020-10-18 17:53
# @Site    : 
# @version : V1.0

import requests
import yaml

def readYaml():
    with open('r', '../data/data.yml', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data

class Base_Reg(object):
    def __init__(self):
        self.ip = 'http://192.168.31.213'
        self.headers = {'X-Requested-With': 'XMLHttpRequest'}

    def post_trmplate(self,url,data,session=requests.session()):
        url = self.ip + url
        resp = session.post(url=url,data=data,headers=self.headers)
        return resp

if __name__ == '__mian__':
    url = '/mtx/index.php?s=/index/user/login.html'
    data = readYaml()
    req = Base_Reg()
    res = req.post_trmplate(url,data)
    print(res.json())