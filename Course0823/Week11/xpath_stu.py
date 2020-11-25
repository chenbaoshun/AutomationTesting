#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : xpath_stu.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-15 15:37
# @Site    : 
# @version : V1.0

from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
url = "http://121.42.15.146:9090/mtx/"
driver.get(url)

# 学习xpath语法，应用到元素查找
# 1.绝对路径：用/开头，从根标签（html）开始
# /html/body/div[6]/div/div/div[2]/a[1]

# 2.相对路径
# //*[@id="syno-nsc-ext-gen3"]/div[6]/div/div/div[2]/a[1]

# 3.索引：如果一个xpath表达式能够找到多个元素，那么可以用[]来选取其中的一个

# 4.通配符‘*’
# 如果不要求标签的话，可以用‘*’代替

# 5.使用“谓语”[]来修饰表达式
# 5.1索引[1]
# 5.2属性[@属性名=属性值]
# 5.3xpath函数[text()=值]

# 6.上下级
'''
ancestor： 先辈
child： 所有子元素(儿子)
descendant： 所有后代(儿子， 孙子， 曾孙子...)
following： 当前标签后的所有节点
parent： 父节点(父亲)
preceding： 当前节点前的所有节点
preceding-sibling： 所有同级的前面节点（ 找弟弟）
following-sibling:所有同级的后面节点（ 哥哥）
'''

# //*[text()='登录']/ancestor::*[@class='header-top']

# 例子
# //div[@class='goods-list']/descendant::a[text()='Meizu/魅族 MX4 Pro移动版 八核大屏智能手机 黑色 16G']
# 先全文搜索找到，class='goods-list'的div标签
# 再从子代里找到text()='Meizu/魅族 MX4 Pro移动版 八核大屏智能手机 黑色 16G'