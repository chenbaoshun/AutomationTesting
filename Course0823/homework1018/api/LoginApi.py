#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : LoginApi.py
# @Author  : Baoshun.Chin
# @Time    : 2020-10-20 22:02
# @Site    : 
# @version : V1.0

import requests
from homework1018.tools.log import Getlog
from homework1018.api.Base_Req import readYaml

class Mtx_Login():
    def __init__(self):
        self.logger = Getlog().get_logger()
        self.url = 'http://192.168.31.213/mtx/index.php?s=/index/user/login.html'
        self.logger.info('实例化Mtx_Login对象')

    def login_suc(self, session=requests.session()):
        accounts = 'chin_mtx'
        pwd = '123456'

        headers = {'X-Requested-With': 'XMLHttpRequest'}
        # data = readYaml()
        data = {'accounts': accounts, 'pwd': pwd}
        resp_login = session.post(url=self.url, data=data, headers=headers)

        self.logger.info(f'登录接口（成功）调用正常:{resp_login}')
        return resp_login,session

    def login_fail(self, session=requests.session()):
        accounts = 'chin'
        pwd = '123456'

        headers = {'X-Requested-With': 'XMLHttpRequest'}
        # data = readYaml()
        data = {'accounts': accounts, 'pwd': pwd}
        resp_login = session.post(url=self.url, data=data, headers=headers)

        self.logger.info(f'登录接口（失败）调用正常:{resp_login}')
        return resp_login, session

if __name__ == '__mian__':
    T = Mtx_Login()
    res,session = T.login_suc()
    print(res.json())
    print(session)