#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_pytest学习.py
# @Author  : Baoshun.Chin
# @Time    : 2020-10-11 14:10
# @Site    : 
# @version : V1.0

# 1.pytest会识别标题为test开头的文件
# 2.pytest会识别类名为Test开头的类
# 3.测试方法需要用test开头

import pytest

class Test_case():
    # 前置方法
    def setup_class(self):
        print('在测试类中只执行一次')

    # 清场方法
    def teardown_class(self):
        print('在测试类所有case运行结束后执行一次')

    def test_case1(self):
        print("执行case1")

    def test_case2(self):
        print("执行case2")

    @pytest.mark.skip
    def test_case3(self):   # 编写检查点
        # 读取数据文件
        # 根据数据请求接口
        # 解析响应中，需要检查的字段
        res = 'this0'
        # 写检查点
        #assert res == 'this'
        assert res == 'this0'
        # pytest原装的assert检查点一旦遇到失败，就会阻塞case继续运行

    @pytest.mark.skip
    def test_case4(self):   # 使用多断言插件
        # pip install pytest-assume(pytest多断言插件)
        # 读取数据文件
        # 根据数据请求接口
        # 解析响应中，需要检查的“字段”
        res = 'this0'
        # 写检查点
        pytest.assume(res == 'this')
        pytest.assume(res == 'this0')

# pytest对参数化的支持，使用@pytest.mark.parametrize装饰器实现
    # 1.单个参数进行参数化
    @pytest.mark.parametrize('passwd',[1234,'abcsdfdsfdfggdgd','','*_28435'])
    def test_passwd_length(self,passwd):
        # 编写检查点
        assert len(passwd) >= 6

    # 2.一组参数的参数化
    data = [[1,2,3],[4,5,8]]
    @pytest.mark.parametrize('var1,var2,res',data)
    def test_parametrize_list(self,var1,var2,res):
        print(f'当前测试的内容是：{var1}+{var2}={res}?')
        data = var1 + var2
        assert data == res

    # 3.使用python库，自动生成参数组合，用于case的参数化


if __name__ == '__main__':
    pytest.main('test_pytest学习')