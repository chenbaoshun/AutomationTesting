#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# @Author  : CHIN
# @Time    : 2020-12-24 22:17

from flask import Flask
from Course0823.Week16.flaskDemo import config

app = Flask(__name__)

# 加载配置文件
app.config.from_object(config)

# 引用视图文件
from Course0823.Week16.flaskDemo import views