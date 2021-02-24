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

# 发送接口请求
id = 2
response = requests.get(""+str(id)).text

# 打开数据库连接
db = pymysql.connect("")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute()方法执行SQL语句
res = cursor.execute("select ")

# 使用fetchone()方法获取一条数据
data = cursor.fetchone()
# 存放的数据库中title的值
print(data[0])

# 提取接口验证点
print(type(response))

# 把字符串类型转换为json类型
result = json.loads(response)
print(result["id"])

# title的验证点
print("title:", result["title"])

# 进行验证点验证
if id == result["id"] and result["title"]==data[0]:
    print("阅读文章接口测试通过")
else:
    print("阅读文章接口测试失败")

# 关闭数据库连接
db.close()