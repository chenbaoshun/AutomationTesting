#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 异形圆.py
# @Author  : Baoshun.Chin
# @Time    : 2020-08-26 21:29
# @Site    : 
# @version : V1.0

import turtle

t = turtle.Pen()
t.shape("turtle")
t.speed(0)
t.pencolor("red")

for i in range(100):
    # t.forward(100)
    # t.left(90)
    t.circle(i)

turtle.done()