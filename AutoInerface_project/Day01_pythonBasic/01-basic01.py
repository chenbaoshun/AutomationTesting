#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 01-basic01.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-19 20:48

# str1 = 'admin'
# help(type(str1))

# name = '''
# hello,你好~
# admin
# tony
# tom
# '''
#
# print(name)
#
# yunyaShare = '雲涯微课堂'
# yunya_share = '雲涯微课堂'
#
# UserManage = '用户管理'

str1='雲涯'
'''编码:str-->bytes'''
str1_bytes=str1.encode('utf-8')
print(str1_bytes)
'''解码:bytes-->str'''
bytes_str1=str1_bytes.decode('utf-8')
print(bytes_str1)

# r.content.encode('gbk')