#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_add_dele.py
# @Author  : Baoshun.Chin
# @Time    : 2020-09-23 22:42
# @Site    : 
# @version : V1.0

from HTMLTestRunner import HTMLTestRunner
import unittest
from Week05.test_demo import add_dele
import time
import os

#构建测试集
suit = unittest.TestSuite()
#测试集加入add_dele文件中被调用的方法。格式suit.addTest(文件名.类名("方法名"))
suit.addTest(add_dele.Test_test("test_shuzi"))
suit.addTest(add_dele.Test_test("test_liangmethod"))

#定义存放测试报告的路径及文件名
#我定义的路径是：当前路径+存放报告的专有目录Report+文件名(文件名是当前时间+report.html)
curent_dirc = os.path.dirname(os.path.realpath(__file__))
report_dirc = "\Report"
now = time.strftime("%Y%m%d-%H%M%S")
report_name = curent_dirc+report_dirc+"\\"+now+"report.html"
fp = open(report_name,"wb")
runner = HTMLTestRunner(stream=fp,
                        title="测试一下报告生成",
                        description="用两个数字的相加减来练习")
runner.run(suit)
fp.close()