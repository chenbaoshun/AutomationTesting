#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : login.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-10 11:41
# @Site    : 
# @version : V1.0

from flask import Flask,jsonify,abort,request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class LoginView(Resource):
    def get(self):
        return {'status': 0, 'msg': 'ok', 'data': '这是一个登录页面'}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help='用户名不能为空')
        parser.add_argument('password', type=str, required=True, help='账号密码不能为空')
        parser.add_argument('age', type=int, help='年龄必须为正整数')
        parser.add_argument('sex', type=str, choices=['男','女'], help='性别只能是男或女')
        args = parser.parse_args()
        return jsonify(args)

api.add_resource(LoginView, '/login', endpoint='login')

if __name__ == '__main__':
    app.run(debug=True)