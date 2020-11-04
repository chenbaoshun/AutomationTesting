#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : httprunner3X_Pa.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-03 21:43
# @Site    : 
# @version : V1.0

import pytest
import csv
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase, Parameters

class Test_httprunner_pa(HttpRunner):
    # @pytest.mark.parametrize("param", Parameters({"var1": ['first', 'second'], "var2": ['random str', 'random  int']}))
    @pytest.mark.parametrize("param", Parameters({"username-password":"${parameterize(data.csv)}"}))
    def test_start(self, param):
        super().test_start(param)

    config = Config('参数化实例').base_url('http://127.0.0.1:5000/').verify(False)

    teststeps = [
        Step(
            RunRequest('joinStr实例接口')
            .get('/joinStr')
            .with_params(**{'str1': '$username', 'str2': '$password'})
            .extract()
            .with_jmespath('body.result', 'res')
                # .with_params(**{'str1': '$var1', 'str2': '$var2'})

        )
    ]

if __name__ == '__main__':
    Test_httprunner_pa().test_start()