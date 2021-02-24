#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : mtx_useraddress.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-02 21:32

from time import sleep
import yaml
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

class Mtx_useraddress():
    def __init__(self,dev):
        self.dev = dev

    with open('../data/user_address.yml') as file:
        data = yaml.safe_load(file)

    # 表达式部分
    add_address = data['add_address']
    address_frame = data['address_frame']
    name_input = data['name_input']
    phone_input = data['phone_input']
    province_select = data['province_select']
    city_select = data['city_select']
    county_select = data['county_select']
    address_input = data['address_input']
    alias_input = data['alias_input']
    is_default = data['is_default']
    save_button = data['save_button']

    # 操作部分
    def save_address(self):
        self.dev.find_element_by_xpath(self.add_address).click()
        sleep(3)
        self.dev.switch_to.frame(self.dev.find_element_by_xpath(self.address_frame))
        name_input = self.dev.find_element_by_name(self.name_input)
        phone_input = self.dev.find_element_by_name(self.phone_input)
        province_select = Select(self.dev.find_element_by_xpath(self.province_select)).select_by_value("2")


if __name__ == '__main__':
    dev = webdriver.Chrome()
    dev.get("http://121.42.15.146:9090/mtx/index.php?s=/index/useraddress/index.html")
    V = Mtx_useraddress(dev)