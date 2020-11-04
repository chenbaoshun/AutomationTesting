#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: Base_Req.py
# @Author: Bull
# ---
# 封装base（基础类、基类）
# 针对MTX商城接口，它的头信息、球球方式、请求方法、ip都可以通用
import requests


class Base_Reg(object):
    def __init__(self):
        self.ip = 'http://121.42.15.146:9090'
        self.headers = {'X-Requested-With': 'XMLHttpRequest'}

    def post_trmplate(self,url,data,session=requests.session()):
        url = self.ip + url
        resp = session.post(url=url,data=data,headers=self.headers)
        return resp

if __name__ == '__main__':
    url = '/mtx/index.php?s=/index/user/login.html'
    data = {'accounts':'bull','pwd':'123456'}
    req = Base_Reg()
    res = req.post_trmplate(url,data)
    print(res.json())