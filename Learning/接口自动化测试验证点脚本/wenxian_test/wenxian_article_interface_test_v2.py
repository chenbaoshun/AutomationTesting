#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : wenxian_article_interface_test_v2.py
# @Author  : BAOSHUNCHIN
# @Email   : baoshunchin@qq.com
# @Time    : 2020-12-12 22:18

# 导入类库
import requests
import json

# 发送接口请求
id = 2
response = requests.get(""+str(id)).text

# 提取接口验证点
print(type(response))

# 把字符串类型转换为json类型
result = json.loads(response)
print(result["status"])

# 进行验证点验证
if result["status"] == str(404):
    print("接口异常测试通过")
else:
    print("接口异常测试失败")