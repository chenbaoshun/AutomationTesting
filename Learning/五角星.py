#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 五角星.py
# @Author  : Baoshun.Chin
# @Time    : 2020-08-26 21:34
# @Site    : 
# @version : V1.0

import turtle

a = 1

t = turtle.Pen()

t.speed(0)
t.pencolor("red")
t.shape("turtle")

a_color = ["red","orange","blue","yellow","green","black"]

for i in range(200):
    t.fd(i)
    t.right(i)

turtle.done()