#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : api.py
# @Author  : CHIN
# @Time    : 2021-01-15

from flask import Flask,jsonify
from flask_restful import Api,reqparse,Resource

app = Flask(__name__)
api = Api(app)

class LoginView(Resource):
	def get(self):
		return {'status':0,'msg':'ok','data':'这是一个登陆页面'}

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('username',type=str,required=True,help='用户名不能为空')
		parser.add_argument('password',type=str,required=True,help='账户密码不能为空')
		parser.add_argument('age',type=int,help='年龄必须为正整数')
		parser.add_argument('sex',type=str,help='性别只能是男或者女',choices=['男','女'])
		args = parser.parse_args()
		return jsonify(args)

api.add_resource(LoginView,'/login',endpoint='login')

if __name__ == '__main__':
    app.run(debug=True,port=5555)