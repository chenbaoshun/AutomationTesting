#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : httpr_stu.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-01 15:30
# @Site    : 
# @version : V1.0

import pytest
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase, Parameters

class Test_hrun_stu(HttpRunner):
    @pytest.mark.parametrize("param", Parameters({"httprunner_version": "$get_httprunner_version()"}))
    def test_start(self, param):
        super().test_start(param)

    config = Config('用来练习的case').base_url('http://127.0.0.1:5000/')

    # @pytest.mark.parametrize("param", Parameters({"username": [111, 222, 333]}))

    teststeps = [
        Step(
            RunRequest('测试getUserName接口')
            .get('/getUserName')
            .extract()
            .with_jmespath('body.username', 'var_username')# 新写一份接口case
            # RunTestCase # 引入一份接口case
        ),
        Step(
            RunRequest('测试joinStr接口')
            .get('/joinStr')
                .with_params(**{'str1': 'hello', 'str2': '$httprunner_version'})
            # .validate()
            #     .assert_equal('body.result', 'hello $var_username')
        ),
        Step(
            RunRequest('测试string_data接口')
            .get('/string_data')
            .extract()
        )
    ]

if __name__ == '__main__':
    Test_hrun_stu().test_start()

    # pytest httpr_stu.py --html=report.html --self -contained -html
    # allure generate report.html -o ./reports/ --clean