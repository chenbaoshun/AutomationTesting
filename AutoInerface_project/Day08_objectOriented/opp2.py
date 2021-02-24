#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : opp2.py
# @Author  : Baoshun.Chin
# @Time    : 2020-12-30 20:28
# @Site    : 
# @version : V1.0

'''
类和继承
'''

# 经典类和新式类的区分，建议所有的类使用新式类，即object

# class A(object):
#     def show(self):
#         print('A')
#
# class B(A):
#     pass
#
# class C(A):
#     def show(self):
#         print('C')
#
# class D(B,C):
#     pass
#
# d = D()
# d.show()

'''
1.__doc__：打印出类的注释
2.__call__:对象创建时直接返回其内容，使用该方法可以模拟静态方法
3.__str__:对象代表的含义，返回一个字符串，通过它可以把对象和字符串关联起来，方便某些程序的实现，
该字符串表示某个类，实现__str__后，可以直接使用print语句输出对象，也可以通过函数str来触发__str__的执行
    （1）对象的意思
    （2）返回一个字符串，字符串和对象关联起来，该字符串表示某个类
'''
# 1.__doc__
class Person(object):
    '''
    对人的定义
    '''
    def info(self,name,age):
        '''
        获取人的信息
        :param name: 姓名
        :param age: 年龄
        :return:
        '''

# print(Person.__doc__)

# 2.__call__
# class P1(object):
#     def __new__(cls, *args, **kwargs):
#         print('call方法')
#
# per = P1()

# 3.__str__
# class Son(object):
#     '''我是一个类'''
#     def __str__(self):
#         return self.__doc__
#
# son = Son()
# # son.__str__()
# print(str(son))

'''
oop工厂设计模式
'''
class Factory(object):
    def createFruit(self,fruit):
        if fruit=='apple':
            return Apple()
        elif fruit=='banana':
            return Banana()
class Fruit(object):
    def __str__(self):
        return 'fruit'

# fruit = Fruit()

class Apple(Fruit):
    def __str__(self):
        return 'apple'

class Banana(Fruit):
    def __str__(self):
        return 'banana'

if __name__ == '__main__':
    factory = Factory()
    print(factory.createFruit('apple'))
    print(factory.createFruit('banana'))