#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : func04.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-16 21:46

'''
返回值：
1.print     None
2.return后面的内容就是函数的返回值
'''

def f():
    print('Hello World')

print(f())

def add(a,b):
    # return a+b
    print(a+b)
print(add(2,3))

'''
应用场景：
1.登录session的应用
'''

def login():
    usename = input('请输入登录账号：\n')
    pwd = input('请输入账号密码：\n')
    if usename=='coco' and pwd=='admin':
        return 'ssfgdhghfjjgggg00982'
    else:
        return '请你登录系统'

def profile(token):
    if token=='ssfgdhghfjjgggg00982':
        print('欢迎你访问雲涯的个人主页')
    else:
        print('你未登录系统，跳转到登录的页面，302')

profile(login())