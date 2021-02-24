#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_mtx_reg.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-02 20:49

import pytest
from selenium import webdriver

from homework1129.page.mtx_reg import Mtx_reg

#pytest的case规则
# 关于setup和teardown的级别:
#     class级别:在每一个测试类执行一次
#     func级别:在每一个测试方法时执行一次

class Test_Mtx_reg():
    def setup(self):
        self.dev = webdriver.Chrome()
        self.dev.get('http://121.42.15.146:9090/mtx/index.php?s=/index/user/reginfo.html')

    #检查在注册页面能正常跳转到"商品搜索"结果页
    def test_into_search(self):
        # 调用封装好的"动作(原子操作)"
        reg_obj = Mtx_reg(self.dev)
        reg_obj.into_search_page('')#这里搜索全部商品
        #设计一个检查点,检查搜索到了全部商品,用查找元素为检查点("//*[@class='goods-images']")
        assert self.dev.find_elements_by_xpath("//*[@class='goods-images']")

    def test_into_search_none(self):#进入到搜索页面,并且没有对应的商品
        # 调用封装好的"动作(原子操作)"
        reg_obj = Mtx_reg(self.dev)
        reg_obj.into_search_page('苹果手机')#这里根据我们的case,来传入一个合适的参数
        #设计一个检查点,检查搜索到了全部商品,用"没有相关数据"这个元素作为检查带你("//i[@class='am-icon-warning']")
        assert self.dev.find_elements_by_xpath("//i[@class='am-icon-warning']")

    def teardown(self):
        self.dev.quit()

if __name__ == '__main__':
    pytest.main()