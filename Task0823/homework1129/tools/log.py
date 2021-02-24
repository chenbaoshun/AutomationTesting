#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : log.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-02 20:46

import logging.handlers

class Getlog():
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

    def get_logger(self):
        fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
        fm = logging.Formatter(fmt)

        tf = logging.handlers.TimedRotatingFileHandler(
            filename = '../log/test.log',
            when = 'H',
            backupCount = 24,
            encoding = 'utf-8'
        )

        #tf处理器，用来写文件
        tf.setFormatter(fm)
        # 给“处理器”设置级别
        tf.setLevel(logging.DEBUG)
        self.logger.addHandler(tf)

        # ch处理器，用来把日志输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(fm)
        self.logger.addHandler(ch)

        return  self.logger

    logger = get_logger()

if __name__ == '__main__':
    logger = Getlog().get_logger()
    logger.debug('日志信息')