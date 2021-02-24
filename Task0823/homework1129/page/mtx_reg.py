#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : mtx_reg.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-02 20:47

from time import sleep
import yaml
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class Mtx_reg():
    def __init__(self,dev):
        self.dev = dev

    with open('../data/mtx_reg.yml', encoding='utf-8') as file:
    # with open('./data/mtx_reg.yml', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    # 表达式部分
    name_input = data['name_input']
    pwd_input = data['pwd_input']
    button = data['button']
    reg_button = data['reg_button']
    assert_reg = data['assert_reg']
    search_input = data['search-input']
    ai_topsearch = data['ai-topsearch']

    #在"页面层里"这里的封装动作,也叫封装"原子操作"
    def name_reg(self,user_name,user_pwd='123456'):
        # 把表达式抽离出来,放到yaml文件中
        # 动作部分
        name_input = self.dev.find_element_by_xpath(self.name_input)
        pwd_input = self.dev.find_element_by_xpath(self.pwd_input)
        button = self.dev.find_elements_by_xpath(self.button)[0]
        reg_button = self.dev.find_elements_by_xpath(self.reg_button)[0]

        sleep(2)
        name_input.send_keys(user_name)
        sleep(2)
        pwd_input.send_keys(user_pwd)
        sleep(2)
        button.click()
        sleep(2)
        reg_button.click()
        element = WebDriverWait(dev,30,0.5).until(lambda e:e.find_element_by_xpath(self.assert_reg))
        return self.dev

    def phone_reg(self,user_name,reg_pwd,user_pwd='123456'):
        pass

    def email_reg(self,user_email,reg_pwd,user_pwd='123456'):
        pass

    def into_search_page(self,text=''):#这个动作,会跳转到搜索商品的结果页
        self.dev.find_element_by_id(self.search_input).send_keys(text)#输入搜索项目
        sleep(2)
        self.dev.find_element_by_id(self.ai_topsearch).click()
        sleep(3)
        return self.dev

if __name__ == '__main__':
    dev = webdriver.Chrome()
    dev.get('http://121.42.15.146:9090/mtx/index.php?s=/index/user/reginfo.html')
    # 在封装case的时候,可以把入口先忽略
    V = Mtx_reg(dev)
    V.into_search_page()