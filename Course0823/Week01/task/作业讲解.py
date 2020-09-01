#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 作业讲解.py
# @Author  : Baoshun.Chin
# @Time    : 2020-08-30 09:54
# @Site    : 
# @version : V1.0

"""
伪代码：
新建变量-每日消费   DayCost=10 / DayCost = input("请输入每日消费金额")
新建变量-乘坐地铁的天数（Days）
新建变量-累计消费
while days < 31:
循环累加 Days：
    如果 累计消费 > 100:
        累计消费 = 累计消费 + 每日消费 * 0.8
    如果累计消费 >= 150:
        累计消费 = 累计消费 + 每日消费 * 0.5
    如果 累计消费 > 400:
        累计消费 = 累计消费 + 每日消费
    如果不和以上的任意情况（else）：
        累计消费 = 累计消费 + 每日消费
"""

Days = int(input('请输入乘车天数:'))
DayCost = float(input('请输入每日消费金额:'))
TotalCost = 0.00   #总消费    #初始化这个变量

for i in range(Days):
    if TotalCost <= 100:
        TotalCost = TotalCost + DayCost
    elif TotalCost > 100 and TotalCost <= 150:
        TotalCost = TotalCost + DayCost * 0.8
    elif TotalCost > 150 and TotalCost <= 400:
        TotalCost = TotalCost + DayCost * 0.5
    else:
        TotalCost = TotalCost + DayCost

print('本月消费总共{}元'.format(TotalCost))