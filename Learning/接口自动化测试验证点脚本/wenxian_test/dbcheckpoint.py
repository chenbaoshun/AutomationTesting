#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : wenxian_article_interface_test_v3.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-12 22:18

# 导入类库
import requests
import json
import pymysql

# 打开数据库连接
db = pymysql.connect("ip", "user", "pwd", "database", charset="utf-8")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute()方法执行SQL语句
res = cursor.execute("select ")

# 使用fetchone()方法获取一条数据
data = cursor.fetchone()
print(data)

# 关闭数据库连接
db.close()