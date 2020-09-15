#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 正方形.py
# @Author  : Baoshun.Chin
# @Time    : 2020-08-26 21:13
# @Site    : 
# @version : V1.0

import turtle

t = turtle.Pen()

t.speed(0)
t.pencolor("red")
t.shape("turtle")
t.pensize(10)

for i in range(100):
    t.forward(i)
    t.left(90)

turtle.done()