#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_api_demo.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-16 21:31

import requests
import pytest

class TestApi():
    def test_yunshi_01(self):
        url = "http://web.juhe.cn:8080/constellation/getAll?consName=金牛座&type=today&key=b4c0cbdedf9727d65f342f9733fa502e"

        headers = {
            'Cookie': 'JSESSIONID=8C8A6339D7ACA15430DE0413EDA7FC26',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        }

        response = requests.request("GET", url=url, headers=headers)

        res = response.json()

        return res

    def test_peidui_02(self):
        url = "http://apis.juhe.cn/xzpd/query?men=%s&women=%s&key=f3eb4ee5e82a4f2e9421c697833ede87" % (
        res['name'][0:2], get_info()['QFriend'][0:2])

        headers = {
            'Cookie': 'JSESSIONID=8C8A6339D7ACA15430DE0413EDA7FC26',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        }

        response = requests.request("GET", url=url, headers=headers)

        print(response.json())

if __name__ == '__main__':
    pytest.main()