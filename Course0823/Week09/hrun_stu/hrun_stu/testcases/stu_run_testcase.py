#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : stu_run_testcase.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-01 16:08
# @Site    : 
# @version : V1.0

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from Week09.hrun_stu.hrun_stu.testcases.httpr_stu import Test_hrun_stu

class stu_run_testcase(HttpRunner):
    config = (
        Config('导入其他测试的例子')
            .base_url('http://127.0.0.1:5000/')
            .verify(False)
            .export(*['username'])
    )

    teststeps = [
        Step(
            RunTestCase('引入练习的测试case')
            .with_variables()
            .call()
            .export('')
        )
    ]