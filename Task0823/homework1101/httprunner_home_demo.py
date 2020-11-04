#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : httprunner_home_demo.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-01 22:21
# @Site    : 
# @version : V1.0

import pytest
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase, Parameters

class Test_hrun_home(HttpRunner):
    @pytest.mark.parametrize("param", Parameters({"username-password":"${parameterize(userData.csv)}"}))
    def test_start(self, param):
        super().test_start(param)

    config = Config('HttpRunner的接口case测试').base_url('http://127.0.0.1:6666/api/v1/admin')

    teststeps = [
        Step(
            RunRequest('注册接口测试')
            .post('/register')
            .with_headers(**{"Content-Type": "application/json"})
            .with_json({'userName': 'root', 'passWord': '123456'})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")

            # .with_jmespath('body.username', 'var_username')# 新写一份接口case
            # # RunTestCase # 引入一份接口case
        ),
        Step(
            RunRequest('登录接口测试')
            .post('/login')
            .with_headers(**{"Content-Type": "application/json"})
            .with_json({'userName': '$username', 'passWord': '$password'})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
        ),
        Step(
            RunRequest('获取时间接口测试')
            .get('/time')
            .extract()
        )
    ]

if __name__ == '__main__':
    Test_hrun_home().test_start()