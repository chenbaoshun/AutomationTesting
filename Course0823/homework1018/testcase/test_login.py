#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_login.py
# @Author  : Baoshun.Chin
# @Time    : 2020-10-20 22:27
# @Site    : 
# @version : V1.0

import pytest
from homework1018.api.LoginApi import Mtx_Login

class Test_login():
    def setup_class(self):
        self.login_obj = Mtx_Login()

    def test_login_suc(self):
        resp_login,session = self.login_obj.login_suc()

        assert resp_login.status_code == 200
        assert resp_login.json().get('msg') == '登录成功'

    def test_login_fail(self):
        resp_login,session = self.login_obj.login_fail()

        assert resp_login.status_code == 200
        assert resp_login.json().get('msg') == '帐号不存在'

    def teardown_class(self):
        self.login_obj = Mtx_Login()

if __name__ == '__main__':
    pytest.main(['-v','--html=./report/report.html'])
    # pytest.main(['-v', '--alluredir', 'report/'])