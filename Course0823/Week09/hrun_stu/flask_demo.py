#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : flask_demo.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-01 15:30
# @Site    : 
# @version : V1.0

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/getUserName', methods=['GET'])
def get_user_name():
    if request.method == 'GET':
        return {
        "info": "这个接口返回一个固定的用户信息",
        "username": "Spike",
        "age": "30",
        "from": "china",
    }

@app.route('/joinStr', methods=['GET'])
def str_join():
    if request.method == 'GET':
        str1 = request.args.get("str1")
        str2 = request.args.get("str2")
        after_join = str1 + " " + str2
        return {
            "info": "这个字符串会把两个参数进行拼接",
            "result": after_join
        }
@app.route('/string_data', methods=['GET'])
def re_str():

    return '就只是字串'


if __name__ == '__main__':
    app.run()