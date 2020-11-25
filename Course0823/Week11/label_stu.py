#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : label_stu.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-15 13:48
# @Site    : 
# @version : V1.0

from time import sleep
from selenium import webdriver

# 练习：分别打开三个标签页，分别进入baidu,sougou,bing这三个网站首页
# 打开标签页没有对应的方法，所以使用js代码来实现
# js_code = f'windows.open("{url}",_blank);'
# dev.execute_script()

# 谷歌浏览启动配置
option = webdriver.ChromeOptions()
# 配置参数 禁止 Chrome 正在受到自动化软件控制
option.add_argument('disable-infobars')
# 配置参数禁止data;的出现
# option.add_argument('user-data-dir=C:\Program Files\Python37\profile')

# 实例化“浏览器”对象
dev = webdriver.Chrome()
url_list = ['https://www.baidu.com/', 'https://www.sogou.com/', 'https://cn.bing.com/']

for i in range(len(url_list)):
    print(f'当前是第{i+1}次循环')
    url = url_list[i]
    js_code = f'window.open("{url}", "_blank");'
    dev.execute_script(js_code)
    print("标签页标题：", dev.title)
    sleep(5)

dev.quit()

