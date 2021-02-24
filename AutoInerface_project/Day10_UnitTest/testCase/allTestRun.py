#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : allTestRun.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-03 00:07
# @Site    : 
# @version : V1.0

import unittest
import os
import HTMLTestRunner
import time

def allTestCases():
    suite = unittest.TestLoader().discover(
        start_dir=os.path.dirname(__file__),
        pattern='test_*.py',
        top_level_dir=None
    )
    return suite

def getNowTime():
    return time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

# print(allTestCases())
def runCases():
    fp = os.path.join(os.path.dirname(__file__),'reports',getNowTime()+'_testReport.html')
    # unittest.TextTestRunner(verbosity=2).run(allTestCases())
    HTMLTestRunner.HTMLTestRunner(
        stream=open(fp,'wb'),
        verbosity=2,
        title='自动化测试报告',
        description='自动化测试报告详细'
    ).run(allTestCases())

if __name__ == '__main__':
    runCases()