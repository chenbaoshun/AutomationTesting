#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : flask_demo.py
# @Author  : Baoshun.Chin
# @Time    : 2020-10-25 16:22
# @Site    : 
# @version : V1.0

import datetime
from flask import Flask,Response,json,request,jsonify
from Week08.LoginDemo.flask_demo_tools import reg_write_csv,login_read_csv

app = Flask(__name__)

# 路由装饰器，描述的是这个“接口”方法（逻辑）对应的URL地址和请求方式（post/get）
@app.route('/register', methods=["POST"])
def register():
    # 编写这个接口的处理逻辑
    # 1.接收和解析数据
    data = json.loads(request.get_data(as_text=True))
    name = data['name']
    pwd = data['pwd']

    # 2.编写这个接口的“逻辑”
    # 把注册信息，存储到文件中
    try:
        if reg_write_csv(name=name, password=pwd):
            data = {'name':name, 'message':'注册成功', 'code':200}
            return jsonify(data)
        else:
            data = {'name': name, 'message': f'用户已存在或用户错误', 'code': 201}
            return jsonify(data)
    except Exception as e:
        print(f'发生异常，原因是{e}')
        data = {'name':name, 'message':f'注册发生异常,原因是：{e}', 'code':204}
        return jsonify(data)

@app.route('/login', methods=["POST"])
def login():
    # 编写这个接口的处理逻辑
    # 1.接收和解析数据
    data = json.loads(request.get_data(as_text=True))
    name = data['name']
    pwd = data['pwd']

    # 2.编写这个接口的“逻辑”
    # 把注册信息，存储到文件中
    try:
        if login_read_csv(name=name, password=pwd):
            data = {'name':name, 'meassage':'登录成功', 'code':200}
            return jsonify(data)
        else:
            data = {'name': name, 'meassage': '用户不存在或密码错误', 'code': 401}
            return jsonify(data)

    except Exception as e:
        data = {'name': name, 'meassage': f'未知异常:{e}', 'code': 402}

@app.route('/time', methods=['GET'])
def get_time():
    now = str(datetime.datetime.now())
    return "当前时间：%s"%now

if __name__ == '__main__':
    app.run(port=5000)