#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : allure装饰器.py
# @Author  : Baoshun.Chin
# @Time    : 2020-10-25 13:05
# @Site    : 
# @version : V1.0

import multiprocessing
import os

import allure
import pytest
import requests


class Test_login:
    ip = 'http://192.168.0.104'
    @allure.title("测试登录步骤")
    @allure.feature("登录模块")#一级
    @allure.story("正常登录")#二级
    @allure.severity("normal")#严重程度
    @allure.step('这是测试的第一步')
    # BLOCKER = 'blocker'　　中断缺陷（客服端程序无响应，无法执行下一步骤）
    # CRITICAL = 'critical'　　临界缺陷（功能点缺失）
    # NORMAL = 'normal'　　普通缺陷（数据计算错误）
    # MINOR = 'minor'　　次要缺陷（界面错误与ui需求不符）
    # TRIVIAL = 'trivial'　　轻微缺陷（必须项无提示，或者提示不规范）
    @allure.link('http://www.testfan.cn/')
    @pytest.mark.parametrize('accounts,pwd,exp', [('chin_mtx', '123456', '登录成功')])
    def test_Decorator (self, accounts, pwd, exp):
        # 登录接口的url
        url = self.ip + '/mtx/index.php?s=/index/user/login.html'
        headers = {'X-Requested-With': 'XMLHttpRequest'}
        data = {'accounts': accounts, 'pwd': pwd}
        r = requests.post(url=url, data=data, headers=headers)
        # print(r.text)
        res = r.json()
        print('头信息')
        print('*'*40)
        print(r.cookies.items())
        assert exp == res['msg']

    @pytest.mark.parametrize('accounts,pwd,exp', [('chin_mtx', '123456', '登录成功')])
    def test_NO_Decorator (self, accounts, pwd, exp):
        # 登录接口的url
        url = self.ip + '/mtx/index.php?s=/index/user/login.html'
        headers = {'X-Requested-With': 'XMLHttpRequest'}
        data = {'accounts': accounts, 'pwd': pwd}
        r = requests.post(url=url, data=data, headers=headers)
        # print(r.text)
        res = r.json()
        print('头信息')
        print('*'*40)
        print(r.cookies.items())
        assert exp == res['msg']


if __name__ == '__main__':
    pytest.main(['allure装饰器.py', '-s', '-q', '--alluredir', './reports'])


# allure serve ./report
# allure generate report/ -o report/html
# pytest allure装饰器.py ‐‐alluredir ./report/allure_raw
# pytest allure装饰器.py -s -q --alluredir ./report