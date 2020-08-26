#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 乘法表.py
# @Author  : Baoshun.Chin
# @Time    : 2020-08-26 21:49
# @Site    : 
# @version : V1.0

for i in range(1,10):
    for j in range(1,i+1):
        print("%s*%s=%s "%(j,i,j*i),end="")
    print()
        # print(j,"*",i,"=",j*i,end="")