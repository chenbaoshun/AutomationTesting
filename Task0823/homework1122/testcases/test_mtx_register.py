#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_mtx_register.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-23 22:26

import pytest
import time
import random
import yaml
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from homework1122.tools.logger import Logger

class Test_Mtx():
    def setup_class(self):

        self.driver = webdriver.Chrome()
        with open('../datas/mtx_reg_elements.yml', encoding='utf-8') as file:
            data = yaml.safe_load(file)
        self.elements = data


    def test_open_register(self):
        url = self.elements['url']
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    def test_mtx_register(self):
        name_input_xpath = self.elements['name_input_xpath']
        name_input = self.driver.find_element_by_xpath(name_input_xpath)

        pwd_input_xpath = self.elements['pwd_input_xpath']
        pwd_input = self.driver.find_element_by_xpath(pwd_input_xpath)

        agreement_choice_xpath = self.elements['agreement_choice_xpath']
        choice_button = self.driver.find_elements_by_xpath(agreement_choice_xpath)[0]

        reg_button_xpath = self.elements['reg_button_xpath']
        reg_button = self.driver.find_elements_by_xpath(reg_button_xpath)[0]

        time.sleep(2)
        account = self.elements['account']
        name_input.send_keys(account)
        time.sleep(2)
        pwd = self.elements['pwd']
        pwd_input.send_keys(pwd)
        time.sleep(2)
        choice_button.click()
        time.sleep(2)
        reg_button.click()

        reg_info = f'//*[text()="{account}，欢迎来到"]'
        user_info = self.driver.find_element_by_xpath(f'//*[text()="{account}"]').get_attribute('span')

        check_info = WebDriverWait(self.driver, 30, 0.5).until(lambda e:e.find_element_by_xpath(reg_info))

        assert user_info in check_info


if __name__ == '__main__':
    t = int(time.time())
    report_name = 'mtx_register_report_' + str(t) + '_' + str(random.randint(0, 100))
    print(report_name)

    pytest.main(['-s', '-v', '--html=../reports/mtx_register_report.html'])
