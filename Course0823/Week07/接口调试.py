#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: 接口调试.py
# @Author: Bull
# ---
import requests

session_var = requests.session()

#调试登录接口
def login(session):
    #1.拼接url
    ip = 'http://192.168.31.213'
    url = '/mtx/index.php?s=/index/user/login.html'
    url = ip+url

    # 2.处理参数
    accounts = 'chin_mtx'
    pwd = '123456'

    # 组装报文
    headers ={'X-Requested-With':'XMLHttpRequest'}
    data = {'accounts':accounts,'pwd':pwd}

    # 3.发送请求
    r = session.post(url=url,data=data,headers=headers)

    # 4.处理响应
    print(r.json())
    return r

def add_cart(session):
    # 1.拼接url
    ip = 'http://192.168.31.213'
    url = '/mtx/index.php?s=/index/cart/save.html'
    url = ip+url

    # 2.处理参数、组装报文
    headers ={'X-Requested-With':'XMLHttpRequest'}
    data = {'goods_id':'6','stock':'1'}

    # 3.发送请求
    r = session.post(url=url, data=data, headers=headers)

    # 4.处理响应
    print(r.json())
    return r

login(session_var)
add_cart(session_var)
