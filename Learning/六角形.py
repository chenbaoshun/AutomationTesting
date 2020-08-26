#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 六角形.py
# @Author  : Baoshun.Chin
# @Time    : 2020-08-26 21:34
# @Site    : 
# @version : V1.0

import turtle

a = 1

t = turtle.Pen()

t.speed(0)
# t.pencolor(color)
t.shape("turtle")

a_color = ["red","orange","blue","purple","green","black"]

# print(a_color[0])

for i in range(200):
    color = a_color[i%6]
    t.pencolor(color)
    t.fd(i)
    t.left(59)

turtle.done()