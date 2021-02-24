#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : yunshi_demo.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-16 20:49

import requests

def get_info():

    url = "http://web.juhe.cn:8080/constellation/getAll?consName=金牛座&type=today&key=b4c0cbdedf9727d65f342f9733fa502e"

    headers = {
      'Cookie': 'JSESSIONID=8C8A6339D7ACA15430DE0413EDA7FC26',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    response = requests.request("GET", url=url, headers=headers)

    # print(response.json()['name'][0:2])
    # print(response.json()['QFriend'][0:2])

    return response.json()

if __name__ == '__main__':
    get_info()