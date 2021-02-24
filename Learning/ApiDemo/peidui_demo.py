#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : peidui_demo.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-16 20:55

import requests

from yunshi_demo import get_info

get_info()

url = "http://apis.juhe.cn/xzpd/query?men=%s&women=%s&key=f3eb4ee5e82a4f2e9421c697833ede87"%(get_info()['name'][0:2],get_info()['QFriend'][0:2])

headers = {
  'Cookie': 'JSESSIONID=8C8A6339D7ACA15430DE0413EDA7FC26',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

response = requests.request("GET", url=url, headers=headers)

print(response.json())

# men = response.json()['men']
men = response.json()['result']['men']
print(men)
assert men == get_info()['name'][0:2]
print('pass')

# assert men == get_info()['QFriend'][0:2]
# print('failure')
# print(response.json()['QFriend'][0:2])