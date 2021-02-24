#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
# @File    : jsonTest.py
# @Author  : CHIN
# @Time    : 2020-12-24 16:44

import json

'''
序列化：把python的数据类型转为str类型的过程
反序列化：str类型转为python的数据类型的过程
'''

# '''字典的序列化与反序列化'''
# dict1 = {'name':'coco','age':18}
#
# # 序列化：dict --> str
# dict_str = json.dumps(dict1)
# print('序列化后的结果：',dict_str,type(dict_str))
#
# # 反序列化：str --> dict
# str_dict = json.loads(dict_str)
# print('反序列化后的结果：',str_dict,type(str_dict))

# '''列表的序列化与反序列化'''
# list1 = ['admin','coco','weike']
#
# # 序列化：list --> str
# list_str = json.dumps(list1)
# print('序列化后的结果：',list_str,type(list_str))
#
# # 反序列化：str --> list
# str_list = json.loads(list_str)
# print('反序列化后的结果：',str_list,type(str_list))

# '''元组的序列化与反序列化'''
# tuple1 = (1,2,3)
#
# # 序列化：tuple --> str
# tuple_str = json.dumps(tuple1)
# print('序列化后的结果：',tuple_str,type(tuple_str))
#
# # 反序列化：str --> list(tuple)
# str_tuple = json.loads(tuple_str)
# print('反序列化后的结果：',str_tuple,type(str_tuple))

'''
{"Result":{"StatusCode":6},"Error":{"code":"s311010018","message":"帐号或密码错误"}}
'''
import requests
# r = requests.post(url='https://www.fxiaoke.com/FHH/EM0HUL/Authorize/PersonalCloudLogin?_fs_token=',
# 				  headers={'content-type': 'application/json',
# 						   'referer': 'https://www.fxiaoke.com/pc-login/build/login.html'},
# 				  data=json.dumps({"phoneNumber": "13938839870","rsaPassword":"TOO6EwX9D4mf3u920MzWU6+Xj+T4p6YXa9UCi/tYlvIAxuN37GsgXCJmvkc6B109eK5gmxH/wvfHUhsXhdCtTx1HWWbA/m3C8KeoNdSW9sMJRorfPHyVdZdDecQNweA7QdeeTCO2QvYDAo/XtAxy44YiYNiOk8AirDwKTAvPn+s="}))
# print(str(r.text))
# print(type(str(r.text)))
# # 反序列化知识：str-->dict
# print(json.loads(str(r.text))['Message'])


'''文件的序列化与反序列化'''
# r = requests.get(url='http://www.weather.com.cn/data/sk/101270101.html')
# # print(r.content.decode('utf-8'))
# # 对文件进行序列化--> 就是把服务端的响应数据写到文件中
# json.dump(r.content.decode('utf-8'),open('weather.json','w'))

# 对文件的反序列化：就是读取文件中的内容
print(json.load(open('weather.json','r')))
dict1 = json.load(open('weather.json','r'))
print(type(dict1))
print('城市：',json.loads(dict1)['weatherinfo']['city'])