#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : fun01.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-10 10:53
# @Site    : 
# @version : V1.0

# def dingding():
#     print('报警')

# def dingding(name):
#     print('报警: {0}'.format(name))
#
# dingding('a')

# def fun2(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# fun2('a', name='chin')
#
# def getData(**kwargs):
#     return kwargs
#
# print(getData(name='A', age=18))
# print(type(getData(name='A', age=18)))

# import requests
# r = requests.get(url='', json=getData())
# r = requests.get(url='', json=getData(name='chin'))
# r = requests.get(url='', json=getData('a', name='chin'))

# def getPost(data):
#     import requests
#     r = requests.post(url='http://127.0.0.1:5000/login',json=data)
#     print(data)
#
# getPost(data=getData(name='A', age=18))

import requests
import json

def login():
    r = requests.post(
        url='http://127.0.0.1:5001/auth',
        json={'username': 'chin', 'password': '123456'}
    )
    return r.json()['access_token']

def getBooks():
    r = requests.get(
        url='http://127.0.0.1:5001/v1/api/books',
        headers={'Authorization': 'jwt {0}'.format(login())}
    )

    # print(json.dumps(r.json(),ensure_ascii='utf-8',indent=True))
    print(r.text)

getBooks()


'''
1.测试驱动的思想
2.UI的自动化测试的应用  核心的流程
3.参数化

共同点  -->  抽离出来
需求：拉勾网添加最新的职位，显示在最前面
1、后台添加不同的职位
2、添加的职位默认展示在第一位
3、搜索的时候，最后添加的也要默认展示在第一位

测试的步骤是一样的
职位不同：
type：
name：
'''