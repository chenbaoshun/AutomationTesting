#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 流程控制.py
# @Author  : Baoshun.Chin
# @Time    : 2020-08-23 0023 15:22
# @Site    : 
# @version : V1.0

# 条件语句
# if语句
# var = input("您需要“鱼”还是“熊掌”？")
# if var == '鱼':
#     print('红烧带鱼')
# if var == '熊掌':
#     print('清蒸熊掌')

# 需求：编写一段代码，来判断年龄是否已满18周岁，来确定是否可以上网
# age = int(input("请输入你的年龄："))                      #接收键盘输入，赋值给变量age，并做数据类型转换
#
# if age >= 18 and age < 60:                                            #输入值和数值18进行比较
#     print("你的年龄是{}，已经成年，可以上网".format(age))
# elif age >= 60:
#     print("你的年龄是{}，也太老了，还是回家休息吧~".format(age))
# else:
#     print("你的年龄是{}，还未成年，还是回家写作业吧~".format(age))

# print格式标准输入
# print('字符串')


# else关键字：

# 标准范式：
# if 表达式:
#     #四个空格或一个tab
#     符合条件时，执行的代码
# else：
#     # 四个空格或一个tab
#     上一个if条件不成立时，执行的代码

# 新增需求：
# 大于60岁时，不建议上网
# elif关键字

# 练习：

# student_age = int(input("请输入学生的年龄："))
#
# if student_age < 10:
#     print("你不是初中生")
# elif student_age >= 10 and student_age < 20:
#     print("初中生,你好！")
#
#     if student_age == 13:
#         print("你是初一学生")
#     elif student_age == 14:
#         print("你是初二学生")
#     else:
#         print("你是初三学生")
# else:
#     print("你是大学生啊！")

# 顺序：从上到下，由左到右

# 分支（if):可以根据条件，略过某些代码

# 循环（while/for）：重复调用一段代码时，可以使用循环
# while循环（条件循环）：
# while 条件:
#   条件满足时，执行 1
#   条件满足时，执行 2
#   条件满足时，执行 3
#   ......

# 实例：计算1-100范围之内的累加的和
# res = 0
# n = 1
#
# while n <= 100:
#     res += n
#     n += 1
#
# print(res)

# 练习:100以内的奇数的累加
# 方案1：
# res = 0
# n = 1
#
# while n <= 100:
#     print(n)
#     res += n
#     n += 2
#
# print(res)

# 方案2：奇数特性：于2整除会余一个数，取模
res = 0
n = 1

while n <= 100:
    if n%2 == 1:
        res += n
    n += 1

print(res)

# for循环：遍历循环
# for 临时变量 in 可迭代对象：
    # 需要循环的代码

for i in 'testfan':

    print(i,end='\n')