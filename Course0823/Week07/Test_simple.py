#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : Test_simple.py
# @Author  : Baoshun.Chin
# @Time    : 2020-10-20 23:13
# @Site    : 
# @version : V1.0

import pytest
import allure

class Test_simple():
    @allure.title('自定义标题')
    @allure.story('登录功能点')
    @allure.severity('阻塞级别')
    def test_case1(self):
        tof = True
        assert tof

    def test_case2(self):
        tof = False
        assert tof

if __name__ == '__main__':
    # pytest.main(["-v","--html=report.html"]
    pytest.main(['-v', '--alluredir', './reports/'])