#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : minigame.py
# @Author  : Baoshun.Chin
# @Time    : 2020-08-23 0023 12:39
# @Site    : 
# @version : V1.0

import random

x = random.randint(1,100)
i = 0

while i<100:
    y = input("请输入数字：")
    print(y)
    y = int(y)
    print(x == y)

    if x==y:
        print("=========")
        print("你猜对了！")
        print("=========")
        break

    elif x>y:
        print("=========")
        print("太大了！")
        print("=========")

    else:
        print("=========")
        print("太小了！")
        print("=========")
