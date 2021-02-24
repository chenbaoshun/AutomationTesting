#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_request_case01.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-10 22:48
# @Site    : 
# @version : V1.0

'''
无依赖性的接口
'''

import requests
import unittest

class ApiTest(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Requests()

    @property
    def test_getToken(self):
        data = {}
        r = self.obj.post()
        return r.json()['access_token']

    @property
    def test_getHeaders(self):
        headers = {}
        return headers

    def test_addBook(self):
        data = {}
        headers = {}
        r = self.obj.post(url='', json=data, headers=self.test_getHeaders)


if __name__ == '__main__':
    unittest.main(verbosity=2)