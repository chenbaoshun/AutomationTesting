#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
# @File    : views.py
# @Author  : CHIN
# @Time    : 2020-12-24 22:18

from Course0823.Week16.flaskDemo.models import *
from Course0823.Week16.flaskDemo import app

@app.route('/')
def hello_word():
	# model操作
	return 'Hello World!'