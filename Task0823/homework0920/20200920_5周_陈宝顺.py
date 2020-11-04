# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@file: 20200920_5周_陈宝顺.py
@time: 2020-09-21 11:00
@author: CHIN
@contact:baoshunchin@qq.com
@version: 1.0.0
"""

'''
一、作业： 
1.根据接口文档和requests库api，自行调试Restful风格的4个接口
Restful风格接口
接口名称	              接口类型	URL	                    参数
Restful-GET类型接口	    GET	    /pinter/com/phone/{id}	手机id
Restful-POST类型接口	    POST	/pinter/com/phone	    {"brand":"Huawei","color":"yellow","memorySize":"64G","cpuCore":"8核","price":"8848","desc":"全新上市"}
Restful-PUT类型接口	    PUT	    /pinter/com/phone	    同上
Restful-DELETE类型接口	DELETE	/pinter/com/phone	    同上 
2.登录我们提供的码同学商城，熟悉商城业务，并尝试编写5条业务流程case
'''

import requests
import random
import json

# 1.根据接口文档和requests库api，自行调试Restful风格的4个接口
print('*'*10 + '调试Restful风格的接口' + '*'*10)
ip = 'http://127.0.0.1:8080'
id_list = ['110','119','120','199']
id = random.choice(id_list)
# print(id)
addr1 = '/pinter/com/phone/'
addr2 = '/pinter/com/phone'
data = {
    "brand":"XiaoMi",
    "color":"yellow",
    "memorySize":"64G",
    "cpuCore":"8核",
    "price":"8848",
    "desc":"全新上市"
}

url1 = ip + addr1 + id
url2 = ip + addr2
# print(url1)
# print(url2)

g = requests.get(url=url1)
print("状态码：",g.status_code)
print(g.text)
print("-"*30)

po = requests.post(url=url2,json=data)
print("状态码：",po.status_code)
print(po.text)
print("-"*30)

pu = requests.put(url=url2,json=data)
print("状态码：",pu.status_code)
print(pu.text)
print("-"*30)

dl = requests.delete(url=url2,json=data)
print("状态码：",dl.status_code)
print(dl.text)
print("-"*30)

# 2.登录我们提供的码同学商城，熟悉商城业务，并尝试编写5条业务流程case
print('*'*10 + '编写5条码同学商城业务流程case' + '*'*10)
mtx_url = 'http://121.42.15.146:9090/mtx/'
houzhui_login = 'index.php?s=/index/user/login.html'
houzhui_logout = 'index.php?s=/index/user/logout.html'
houzhui_search = 'index.php?s=/index/search/index.html'
houzhui_reg = 'index.php?s=/index/user/reg.html'

reg_url = mtx_url + houzhui_reg
login_url = mtx_url + houzhui_login
logout_url = mtx_url + houzhui_logout
search_url = mtx_url + houzhui_search

reg_data = {
    "accounts": "chin_mtx",
    "pwd": "123456",
    "type": "username",
    "is_agree_agreement": "1"
}

login_data = {
    "accounts": (None, "chin_mtx"),
    "pwd": (None, "123456")
}

search_data = {
    "wd": (None, "iPhone")
}

headers = {
    'Content-Type': 'application/json'
}

# 1-访问商城
fangwen = requests.get(url=mtx_url)
print('状态码：',fangwen.status_code)
# print(fangwen.text)
print("-"*30)

# 2-用户注册
user_register = requests.post(url=reg_url, data=json.dumps(reg_data), headers=headers)
print('状态码：',user_register.status_code)
# print(user_register.json())
print(user_register.text)
print("-"*30)

# 3-用户登录
user_login = requests.post(url=login_url, data=json.dumps(login_data), headers=headers)
print('状态码：',user_login.status_code)
# print(user_login.json())
print("-"*30)

# 4-用户退出
user_logout = requests.get(url=logout_url)
print('状态码：',user_logout.status_code)
# print(user_logout.json())
print("-"*30)

# 5-搜索商品
secrch = requests.post(url=search_url, files=search_data)
print('状态码：',secrch.status_code)
# print(secrch.json())
print("-"*30)