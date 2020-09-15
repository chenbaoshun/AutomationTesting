#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_data.py
# @Author  : Baoshun.Chin
# @Time    : 2020-09-05 20:18
# @Site    : 
# @version : V1.0

import csv
import datetime
from faker import Faker

# 整合代码
pre = 'teacher'
file = open("教师信息测试数据文件.csv","w",newline="")
faker = Faker(locale="zh_CN")

for i in range(1,2):
    num = str(i).zfill(4)
    tloginid = pre + num
    tloginname = faker.name()
    starttime = datetime.date.today()
    endtime = faker.date_between(start_date = "today",end_date = "+20d")
    idcard = faker.ssn(min_age=18,max_age=50)
    phonenumber = faker.phone_number()
    email = faker.email()
    fwrite = csv.writer(file)
    fwrite.writerow([tloginid,tloginname,starttime,endtime,idcard,phonenumber,email])

file.close()

# 实验1.生成随机教师登录名
# pre = 'stl'
# file = open("教师信息测试数据文件.csv","w",newline="")
#
# for i in range(1,11):
#     # print(i)
#     num = str(i).zfill(5)
#     # print(num)
#     tloginid = pre + num
#     fwrite = csv.writer(file)
#     fwrite.writerow([tloginid])
#     # print(tloginid)
#
# file.close()

# 实验2.将数据保存到文件（文件名：教师信息测试数据文件.csv）
# file = open("教师信息测试数据文件.csv","w")
# 获取写文件的对象
# fwrite = csv.writer(file)
# # 写入内容
# fwrite.writerow(["sdhfjsdfj","131242"])
# # 关闭文件
# file.close()

# # 实验3.随机生成汉字-教师名
# faker = Faker(locale="zh_CN")
# tloginname = faker.name()
# print(tloginname)
#
#
# # 实验4.开始时间
# start = datetime.date.today()
# print(start)
#
# # 实验5.结束时间
# faker = Faker(locale="zh_CN")
# endtime = faker.date_between(start_date = "today",end_date = "+20d")
# print(endtime)

# # 实验6.随机生成身份证号
# idcard = faker.ssn()
# print(idcard)
#
#
# # 实验7.随机生成手机号
# phonenumber = faker.phone_number()
# print(phonenumber)
#
# # 实验8.随机生成邮箱地址
# email = faker.email()
# print(email)

# idcard = faker.credit_card_number(card_type=None)
# print(idcard)
