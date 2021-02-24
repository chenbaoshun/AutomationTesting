#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : rest01.py
# @Author  : CHIN
# @Time    : 2021-01-24

from flask import Flask,make_response,jsonify,abort,request
from flask_restful import Api,Resource
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app=app)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(name):
	if name=='chin':
		return 'admin'

@auth.error_handler
def authorized():
	return make_response(jsonify({'message':'请认证'}),401)

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'status':404,'error':'访问页面不存在'}),404)

@app.errorhandler(405)
def not_found(error):
	return make_response(jsonify({'status':405,'error':'该方法只支持GET请求'}),405)

@app.errorhandler(500)
def not_found(error):
	return make_response(jsonify({'status':500,'error':'请耐心等待，服务正在修复中'}),500)

books = [
    {'id':1,'author':'tester','name':'Python接口自动化测试实战','done':True},
    {'id':2,'author':'测试菌','name':'Python接口自动化测试入门','done':False},
    {'id':3,'author':'chin','name':'Selenium3自动化测试实战','done':True},
    {'id':4,'author':'陈','name':'Selenium3自动化测试入门','done':False}
]

@app.route('/v1/api/books',methods=['GET'])
def get_books():
	return jsonify(books)

@app.route('/v1/api/books',methods=['POST'])
def create_books():
	if not request.json:
		abort(400)
	else:
		book = {
			'id': books[-1]['id'] + 1,
			'author': request.json.get('author'),
			'name': request.json.get('name'),
			'done': True
		}
		books.append(book)
		return jsonify({'message':'添加成功'},201)

if __name__ == '__main__':
    app.run(debug=True,port=8000)