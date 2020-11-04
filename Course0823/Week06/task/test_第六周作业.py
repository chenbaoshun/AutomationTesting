#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020-10-13 15:48
# @Author  : lanjiali
# @File    : test_第六周作业.py

# 1.使用pytest编写5条商城接口测试case

import pytest
import  requests

ip = 'http://121.42.15.146:9090'
class Test_mtxshop():

    #注册case
    # 1.未注册的账号：符合规范的用户&密码
    # 2.用户名不正确，密码符合规范
    # 3.已注册的账号，再次注册
    # @pytest.mark.skipif
    @pytest.mark.parametrize('accounts,pwd,type,is_agree_agreement,result',
                             [
                                 ('abc123','123456abc','username','1','注册成功'),
                                 ('s','123456','username','1','用户名格式由 字母数字下划线 2~18 个字符'),
                                 ('_abc','12345','username','1','账号已存在')
                             ])
    def test_reg(self,accounts,pwd,type,is_agree_agreement,result):
        #注册接口
        url = ip + '/mtx/index.php?s=/index/user/reg.html'
        headers = {
            'X-Requested-With': 'XMLHttpRequest'
        }
        data = {
            'accounts':accounts,
            'pwd':pwd,
            'type':type,
            'is_agree_agreement':is_agree_agreement
        }
        res = requests.post(url=url,data=data,headers=headers)
        r =res.json()
        print(r)
        print(r['msg'])
        assert result == r['msg']


    # 登录case
    # 1.正确的用户名和密码登录
    # 2.正确的用户名和错误的密码登录
    # 3.错误的用户名和错误的密码
    # 4.未注册的账号登录
    # @pytest.mark.skipif
    @pytest.mark.parametrize('accounts,pwd,result',
                             [
                                 ('1234','123456','登录成功'),
                                 ('1234','!123478@','密码错误'),
                                 ('123A','123456L','帐号不存在'),
                                 ('@12345','abcdefg','帐号不存在')])
    def test_login(self,accounts,pwd,result):
        # 登录接口
        url = ip + '/mtx/index.php?s=/index/user/login.html'
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
                   }
        data = {
            'accounts':accounts,
            'pwd':pwd
        }
        res = requests.post(url=url,data= data,headers=headers)
        # print(res.text)
        r = res.json()
        print(r)
        assert result == r['msg']




