#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
# @File    : app.py
# @Author  : CHIN
# @Time    : 2020-12-24 14:17

from flask import Flask,make_response,jsonify,abort,request
from flask_restful import Api,Resource
from flask_httpauth import HTTPBasicAuth

from flask import Flask
from flask_jwt import JWT,jwt_required,current_identity

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'
api = Api(app=app)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(name):
	if name=='admin':
		return 'admin'

@auth.error_handler
def authorized():
	return make_response(jsonify({'msg':'请认证！'}),403)

books = [
	{'id':1,'author':'abu','name':'Python接口自动化测试实战','done':True},
	{'id':2,'author':'雲涯','name':'selenium自动化测试实战','done':False}
]

