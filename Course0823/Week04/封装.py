#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: 封装.py
# @Author: Bull
# ---
# 对于类名：
# 1.见名知意
# 2.一般来说，要求类名的首字母大写
# 3.定义类的三种写法
# 1.
# class Plane():

# 2.
# class Plane:

# 3.
# class Plane(object):

# 类的属性
# 1.类属性
# 2.实例属性

# 类的方法
# 1.要求入参必须传一个self关键字
# 2.在调用类的属性或者类的其他方法时也要带self

# class Plane:
#     lenth = 400
#     weight = 500
#
#     def down(self):
#         print('降落')
#
#     def fly(self):
#         print('我会飞')
#
# #创建对象 或者叫 实例化
# plane1 = Plane()
# plane2 = Plane()
# #
# # plane2.fly()
# # print(plane2.lenth)
#
# print(Plane.lenth)
#
# # plane1.fly()

# 类属性 和 实例属性
# 类属性：    近似于一个类里边共用的常量。不建议大家修改类的属性
# 实例属性：  可以动态接收调用时传参，编码的时候使用__init__()-实际上是python的魔法方法
class Dog:
    # def __init__(self,age):
    #     self.age = age
    __touth = 10

    def __init__(self,age):
        self.age = 5
        self.age2 = age
        print('执行类的初始化方法-__init__')
        def func1():
            print('init里的子方法')
        func1()

    def info_print(self):
        print(self.age)
        print(f'init函数里直接给了值:{self.age}')
        print(f'接收到的age:{self.age2}')


    def print_name(self,name):
        print(f'我的名字是{name}')


    @classmethod#装饰器的语法，会对下一行开始的方法生效
    def get_tooth(cls):
        print(cls.__touth)

    @staticmethod
    def static_info_print(name):
        print(f'这是一个描述狗子的类，{name}')

# wangcai = Dog(age=6)
# # print(wangcai.age)
# # wangcai.info_print()
# wangcai.print_name('旺财')

# 调试类方法
# Dog.get_tooth()

# 调试静态方法
# wangcai = Dog(4)
#静态方法既可以使用对象访问又可以使用类访问
# wangcai.static_info_print('旺财')
Dog.static_info_print('旺财')

# 类里边的语法
# 类名的三种定义写法
# 类属性的定义
# 实例化属性的定义 和 接收参数（重点）*魔法方法
# *修改类属性（在后边用到时候讲，它是一个容易出现混淆的写法）
# 类之中普通方法的传参
# 类方法 和 静态方法，可以跳过实例化直接使用类里写好的方法