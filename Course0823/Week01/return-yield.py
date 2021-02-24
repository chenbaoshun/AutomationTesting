#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : return-yield.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-06 22:11

# def foo(num):
#   print("starting...")
#   while num<10:
#     num=num+1
#     yield num
# for n in foo(0):
#   print(n)

def foo(num):
  print("starting...")
  while num<10:
    num = num+1
    return num
for n in foo(0):
  print(n)

# def foo():
#     print("starting...")
#     while True:
#        res = 4
#        return res
#        print("res:", res)
#
# g = foo()
# print(next(g))
# print("*"*20)
# print(next(g))