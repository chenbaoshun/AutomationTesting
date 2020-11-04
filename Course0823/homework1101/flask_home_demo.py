#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : flask_home_demo.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-10-26 23:38
# @Site    : 
# @version : V1.0

import datetime
import time
from flask import Flask,Response,json,request,jsonify
from homework1025.file_tools import read_user_csv, write_user_csv, read_username, create_user_csv

app = Flask(__name__)

# 路由装饰器，描述的是这个“接口”方法（逻辑）对应的URL地址和请求方式（post/get）
@app.route('/api/v1/admin/register', methods=["POST"])
def register():
    # 编写这个接口的处理逻辑
    # 1.接收和解析数据
    data = json.loads(request.get_data(as_text=True))
    userName = data['userName']
    passWord = data['passWord']

    # 2.编写这个接口的“逻辑”
    # 把注册信息，存储到文件中
    try:
        in_name = read_username(userName)
        if in_name:
            data = {'username': userName, 'message': '注册成功', 'code': 1000}
            create_user_csv()
            write_user_csv(username=userName, password=passWord)
            return jsonify(data)
        else:
            data = {'username': userName, 'message': f'用户名已存在,请重新输入...', 'code': 1001}
            return jsonify(data)

    except Exception as e:
        # print(f'发生异常，原因是{e}')
        data = {'message':f'注册发生异常,原因是：{e}', 'code':1004}
        return jsonify(data)

@app.route('/api/v1/admin/login', methods=["POST"])
def login():
    # 编写这个接口的处理逻辑
    # 1.接收和解析数据
    data = json.loads(request.get_data(as_text=True))
    userName = data['userName']
    passWord = data['passWord']
    time_stamp = str(int((time.time()*1000)))
    userToken = userName + time_stamp

    # 2.编写这个接口的“逻辑”
    # 从存储文件中读取登录信息
    try:
        if read_user_csv(username=userName, password=passWord):
            data = {'username':userName, 'usertoken': userToken, 'message':'登录成功', 'code':2000}
            return jsonify(data)
        else:
            data = {'username':userName, 'message': '用户不存在或密码错误', 'code': 2001}
            return jsonify(data)

    except Exception as e:
        data = {'username':userName, 'message': f'登录发生未知异常:{e}', 'code': 2002}
        return jsonify(data)

@app.route('/api/v1/admin/time', methods=['GET'])
def get_time():
    try:
        t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        data = {'time': t, 'message': '获取当前时间成功', 'code': 200}
        return jsonify(data)
    except Exception as e:
        data = {'message': f'获取当前时间发生未知异常:{e}', 'code': 2002}
        return jsonify(data)


if __name__ == '__main__':
    app.run(port=6666)