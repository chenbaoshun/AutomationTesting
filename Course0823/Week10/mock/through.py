#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : through.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-08 11:21
# @Site    : 
# @version : V1.0

# 实现各种透传方法
import requests
from flask import json,make_response

url_t ='http://127.0.0.1:5000/'#透传需要调用的“真实”服务的地址

#方式1：参数透传
def passThrough(url,data):
    url = url_t + url
    print(url)
    res = requests.post(url,json=data)
    #透传实际上用requests库从代码里调用一下真实服务

    resp = make_response(res.json())
    #把requests请求的响应进行处理，然后作为mock透传的“响应数据”
    return resp

# 方式2：接口级别的透传
def passThroughRe(url,data):
    url = url_t + url
    print(url)
    res = requests.post(url=url,json=data)
    resp = make_response(res.json())
    return resps