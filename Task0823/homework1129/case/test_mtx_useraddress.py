#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_mtx_useraddress.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-02 21:32

import pytest
from selenium import webdriver

from homework1129.page.mtx_useraddress import Mtx_useraddress

class Test_Mtx_useraddress():
    def setup(self):
        self.dev = webdriver.Chrome()
        self.dev.get('http://121.42.15.146:9090/mtx/index.php?s=/index/useraddress/index.html')

    def test_save_address(self):
        self.dev.find_element_by_xpath()

    def teardown(self):
        self.dev.quit()

if __name__ == '__main__':
    pytest.main()

