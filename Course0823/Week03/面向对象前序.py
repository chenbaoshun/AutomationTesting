#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 面向对象前序.py
# @Author  : Baoshun.Chin
# @Time    : 2020-09-06 15:28
# @Site    : 
# @version : V1.0

# 举例：如果需求变更为接收字符串变量，而不是键盘输入
# 函数式的做法，可能需要重写整个方法
# 面向对象的话，只需要去修改输入的方法

# class words():  #这个类用来统计单词在短语中出现的频率
#     def input_back(self):    #处理键盘输入的放大
#         pass
#     def input(self):    #接收字符串变量
#         pass
#     def rep_string(self):   #统一字符串分隔符的方法
#         pass
#     def to_dict(self):  #将词频统计到字典
#         pass

# 练习题1
# 需求：
# - 小明今年18岁，身高1.75，每天早上跑完步，会去吃东西
# - 小美今年17岁，身高1.65，小美不跑步，小美喜欢吃东西

# 考点：按照面向对象的思路，对这个需求点进行分析

# 分析：
# 1.两条需求都是描述“分类”
# 2.都有人名
# 3.都有年龄
# 4.都描述了身高
# 5.1.小明具有“跑步”和“吃东西”两个事务
# 5.2.小明具有“吃东西”这个事务

# 伪代码
# class 人类():
#     类的属性：
#     name = '小明'
#     age = 18
#     heigh = 175
#
#     def run(self):
#         pass
#     def eat(self):
#         pass
#
# class person():

# 练习2
# 需求：
# - 一只黄颜色的狗狗叫大黄
# - 看见生人汪汪叫
# - 看见家人摇尾巴

# 狗
# 颜色
# 名字
# 生人 - 旺旺叫
# 家人 - 摇尾巴

class Dog():
    name = '大黄'
    color = 'yellow'
    def shake(self):
        print('见到家人，好开心')
    def shout(self):
        print('生人勿近，汪汪汪')

    def main(self,moment):
        if moment == '生人':
            self.shout()
        elif moment == '家人':
            self.shake()

dog = Dog()
dog.main('生人')