#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : 字符串.py
# @Author  : Baoshun.Chin
# @Time    : 2020-08-30 10:37
# @Site    :
# @version : V1.0

# 直接赋值
# ①单引号 - ''
# name = 'tim'
# ②双引号 - ""
# name = "tim"
# ③三引号（三对单引号和三对双引号）
# name = '''tim'''
# name = """tim"""
# *三引号形式的字符串支持换行
# text = '''this is
# a text'''
# text = """
# this is
# a text
# """

# 转义符 \
# ①取消字符的特殊含义
# 例1：
# var = 'I\'m tom'
# print(var)
# ②字符引用-实现特殊的文本编辑功能
# 例2：
# import time
# for i in range(10):
#     print("\r离程序退出还剩%s秒" % (9-i), end="")   #\r的功能是换行（行首）
#     time.sleep(1)

# 使用input()方法进行赋值
# user_name = input()
# 如果用文字描述input()的功能：
#     等待计算机的键盘输入
#     一旦敲下回车键
#     就把所有接受的键盘输入，返回 - 一个字符串
#     *附件功能：
#         可以将该变量的提示信息输出在控制台作为“参数”，输出到控制台
# user_name = input('请输入姓名：')

# 字符串拼接
# agreement = 'http://'
# ip = "121.42.15.146:9090"   #码同学实战商城
# url = "/mtx/"
# # ①字符串加法:使用+进行字符串拼接（类型需一致）
# # print(agreement+ip+url)
# # ②join:将“参数”整合成一个“字符串”结果并返回
# list = agreement,ip,url
# print(type(list))
# str3 = ''.join(list)
# print(str3)
# ③f''

# 序列
# 索引从0开始
# 可变 不可变-内存地址
# v = "我是A"
# print(v)
# print(id(v))
#
# v = "我是B"
# print(id(v))
# 字符串的下标 - 通过“下标”去取字符串的某个字符
# name = 'testfan'
# print(name)
# print(name[0])
# print(name[1])
# # 也可以使用负数
# print(name[-1])
# 下标从0开始
# * -号 可以决定索引的方向

# 切片
# 序列名称(序列变量名)[切片开始的位置:切片结束的位置:*可选参数（步长）]
# 切片截取的规则：左闭右开
# print(name[2:5])
# print(name[2:5:2])
# # print(name[-2:])
# print(name[-5:])    #从倒数第5位开始到最后
# print(name[:-1])    #从0开始到倒数第2位
# print(name[::-2])   #反转
# print(name[::1])
# print(name[-3:])
# print(name[2:-3])

# 遍历字符串的下标
# for i in name: #可迭代对象
#     print(i)

# len -用来返回序列的元素数量
# for i in range(len(name)):
#     print(name[i])
#     print(i)

# for i in name:
#     if i == 't':
#         print('特殊处理')

# 字符串方法
# ①查找-find()：检测某个字符串是否在某个字符串中，如果在，就返回子串开始位置的下标，否则，返回-1
# 字符串序列.find(子串,开始位置下标，结束位置下标)
str= ',hello world and testfan and yaoyao,'
# print(str.find('and'))
# *index(): 检测某个子串是否包含在这个字符串中，如果在则返回这个子串开始位置的索引位置，不在则会报异常
# print(str.index('andw'))
# print(str.rindex('and'))
# print(str.rfind('and'))
# # 出现的次数
# print(str.count('and'))
# # ②替换-replace()：
# # 字符串序列.replace(旧子串，新子串，替换次数)
# print(str.replace('world','python',1))
# print(str.replace('and','和',9))
# print(str.replace(__old='and',__new='和'))
# ③分隔-split():分割字符串
# str= 'hello,world,and,testfan,and,yaoyao'
# str1= 'hello world and testfan and yaoyao'
# print(str.split(','))
# print(str1.split(' ',2))

# 修改
# print(str.capitalize())   #将字符串第一个字符串转换成大写
# str1 = str.title()    #将字符串每个单词首字母转换成大写
# print(str1)
# print(str1.lower())   #将字符串中大写转小写
# print(str.upper())    #将字符串中小写转大写
# print(str.lstrip(','))    #删除字符串左侧空白字符
# print(str.rstrip(','))    #删除字符串右侧空白字符
print(str.strip(','))  #删除字符串两侧空白字符
s = 'hello 123lo'
print(s.ljust(10,'-'))  #原字符串左对齐，并使用指定字符（默认空格）填充至对应长度的新字符串
print(s.center(11,'*')) #原字符居中对齐，并使用指定字符(默认空格)填充对应长度的字符串

# 判断
print(s.startswith('he'))   #检查字符串是否是以指定子串开头，是则返回True，否则返回False。如果设置开始和结束位置下标，则在指定范围内检查
print(s.startswith('er'))
print(s.endswith('lo')) #检查字符串是否是以指定子串结尾，是则返回True，否则返回False。如果设置开始和结束位置下标，则在指定范围内检查
print(s.isalpha())  #如果字符串至少有一个字符并且所有的字符都是字母则返回True，否则返回False
print(s.isdigit())  #如果字符串只包含数字则返回True，否则返回False
print(s.isalnum())  #如果字符串中至少有一个字符并且所有的字符是字母或者数字则返回True,否则返回False
print(s.isspace())  #如果字符串中只包含空白，则返回True，否则返回False