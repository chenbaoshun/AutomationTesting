#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : log.py
# @Author  : Baoshun.Chin
# @Time    : 2020-10-18 16:35
# @Site    : 
# @version : V1.0

import logging
import logging.handlers


class Getlog():
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            cls.logger = logging.getLogger()
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)

        tf = logging.handlers.TimedRotatingFileHandler(
            filename='../log/test.log',
            when='S',
            backupCount=5,
            encoding='utf-8'
        )

        # tf处理器，用来写文件
        tf.setFormatter(fm)

        # 给“处理器”设置级别
        tf.setLevel(logging.INFO)
        self.logger.addHandler(tf)

        # ch处理器，用来把日志输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(fm)
        self.logger.addHandler(ch)

        return self.logger

if __name__ == '__main__':
    logger = Getlog().get_logger()
    logger.info('日志信息')
