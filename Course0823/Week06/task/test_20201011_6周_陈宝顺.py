#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_20201011_6周_陈宝顺.py
# @Author  : Baoshun.Chin
# @Time    : 2020-10-11 22:32
# @Site    : 
# @version : V1.0

# 一、作业：
# 1.使用pytest编写5条商城接口测试case

import pytest
import requests
# import yaml

ip = 'http://121.42.15.146:9090'

class Test_mtx_case():
    def setup_class(self):
        print('开始执行case')

    # 注册case
    # 1.未注册的账号：符合规范的用户&密码
    # 2.用户名不正确，密码符合规范
    # 3.已注册的账号，再次注册
    # @pytest.mark.skip
    @pytest.mark.parametrize('accounts,pwd,type,is_agree_agreement,result',
                             [
                                 ('chin123', 'abc123456', 'username', '1', '注册成功'),
                                 ('s', '123456', 'username', '1', '用户名格式由 字母数字下划线 2~18 个字符'),
                                 ('_abc', '12345', 'username', '1', '账号已存在')
                             ])
    def test_register(self, accounts, pwd, type, is_agree_agreement, result):
        # 注册接口
        url = ip + '/mtx/index.php?s=/index/user/reg.html'
        headers = {
            'X-Requested-With': 'XMLHttpRequest'
        }
        data = {
            'accounts': accounts,
            'pwd': pwd,
            'type': type,
            'is_agree_agreement': is_agree_agreement
        }
        res = requests.post(url=url, data=data, headers=headers)
        r = res.json()
        print(r)
        print(r['msg'])
        assert result == r['msg']

    # 登录case
    # 1.正确的用户名和密码登录
    # 2.正确的用户名和错误的密码登录
    # 3.错误的用户名和错误的密码
    # 4.未注册的账号登录
    # @pytest.mark.skip
    @pytest.mark.parametrize('accounts,pwd,result',
                             [
                                 ('1234', '123456', '登录成功'),
                                 ('1234', '!123478@', '密码错误'),
                                 ('123A', '123456L', '帐号不存在'),
                                 ('@12345', 'abcdefg', '帐号不存在')])
    def test_login(self, accounts, pwd, result):
        # 登录接口
        url = ip + '/mtx/index.php?s=/index/user/login.html'
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
        }
        data = {
            'accounts': accounts,
            'pwd': pwd
        }
        res = requests.post(url=url, data=data, headers=headers)
        # print(res.text)
        r = res.json()
        print(r)
        assert result == r['msg']

    def teardown_class(self):
        print('case执行完毕')

if __name__ == '__main__':
    pytest.main('test_20201011_6周_陈宝顺.py')