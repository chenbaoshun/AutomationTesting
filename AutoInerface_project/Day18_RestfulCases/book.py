#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : book.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-03 22:50

from flask import Flask,make_response,jsonify,abort,request
from flask_restful import Api,Resource
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app=app)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(name):
    if name=='admin':
        return 'admin'

@auth.error_handler
def authorized():
    return make_response(jsonify({'msg':'请认证'}),401)

books = [
    {'id':1,'author':'tester','name':'Python接口自动化测试实战','done':True},
    {'id':2,'author':'测试菌','name':'Python接口自动化测试入门','done':False},
    {'id':3,'author':'chin','name':'Selenium3自动化测试实战','done':True},
    {'id':4,'author':'陈','name':'Selenium3自动化测试入门','done':False}
]

class Books(Resource):
    def get(self):
        return jsonify({'status':0,'msg':'查询成功','datas':books})

    def post(self):
        if not request.json:
            return jsonify({'status':1001,'msg':'请求参数不是json格式，请检查后重试！'})
        else:
            book = {
                'id':books[-1]['id'] + 1,
                'author':request.json.get('author'),
                'name':request.json.get('name'),
                'done':True
            }
            books.append(book)
            return jsonify({'status':1002,'msg':'添加书籍成功','datas':book},201)

class Book(Resource):
    def get(self,book_id):
        book = list(filter(lambda t:t['id']==book_id,books))
        if len(book)==0:
            return jsonify({'status':1003,'msg':'很抱歉，你查询的书籍不存在，请核对后再试！'})
        else:
            return jsonify({'status':0,'msg':'查询成功','datas':book})

    def put(self,book_id):
        book = list(filter(lambda t:t['id']==book_id,books))
        if len(book)==0:
            return jsonify({'status':1003,'msg':'很抱歉，你查询的书籍不存在'})
        elif not request.json:
            return jsonify({'status':1001,'msg':'请求参数不是json格式，请检查后重试！'})
        elif 'author' not in request.json:
            return jsonify({'status':1004,'msg':'请求参数author不能为空'})
        elif 'name' not in request.json:
            return jsonify({'status':1005,'msg':'请求参数name不能为空'})
        elif 'done' not in request.json:
            return jsonify({'status':1006,'msg':'请求参数done不能为空'})
        elif type(request.json['done'])!=bool:
            return jsonify({'status':1007,'msg':'请求参数done为bool类型'})
        else:
            book[0]['author'] = request.json.get('author',book[0]['author'])
            book[0]['name'] = request.json.get('name', book[0]['name'])
            book[0]['done'] = request.json.get('done', book[0]['done'])
            return jsonify({'status':1008,'msg':'更新书籍信息成功','datas':book})

    def delete(self,book_id):
        book = list(filter(lambda t:t['id']==book_id,books))
        if len(book)==0:
            return jsonify({'status':1003,'msg':'很抱歉，你查询的书籍不存在'})
        else:
            books.remove(book[0])
            return jsonify({'status':1009,'msg':'书籍删除成功'})

api.add_resource(Books,'/v1/api/books')
api.add_resource(Book,'/v1/api/book/<int:book_id>')

if __name__ == '__main__':
    app.run(debug=True)