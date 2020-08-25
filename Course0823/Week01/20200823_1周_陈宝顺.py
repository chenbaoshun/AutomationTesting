#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 20200823_1周_陈宝顺.py
# @Author  : 陈宝顺
# @Time    : 2020-08-23 0023 22:19
# @version : V1.0

'''
作业：
需求如下：
以一个月为期限，
一张一卡通乘坐北京轨道交通累计消费满100元后，下一次开始乘车时有8折优惠；
满150元后，下一次开始乘车时有5折优惠；
支出累计达到400元后，就将不再享受打折优惠。
一卡通卡轨道交通支出累计记录每自然月底清零,下自然月重新累计
题目：
编写代码计算：
每日无折扣票价10元
每月上班21天
一个月需要花费多少钱地铁费？
Day1：10
Day2：10+10 <100
Day3：20+10 <100
……
计算一个月乘坐地铁的总共花费？
'''


cost = 0											#设置变量cost记录用户在地铁上的消费情况（元）
day = 1												#设置变量day记录天数
# money = 0

# print(type(cost))

while day <= 21:									#共21天
    rate = 0.0										#设置变量rate记录优惠率
    cost += 10

    if cost == 100:
        rate = 0.8
        cost = cost + 10 * rate
        # print(cost1)

    elif cost == 150:
        rate = 0.5
        cost = cost + 10 * rate
        # print(cost2)
    else:
        rate = 1.0
        cost = cost + 10 * rate
        # print(cost3)

    day += 1

# money = cost + cost1 + cost2 + cost3

# print(money)


print("您当月乘坐地铁的花费总共为{}".format(cost))