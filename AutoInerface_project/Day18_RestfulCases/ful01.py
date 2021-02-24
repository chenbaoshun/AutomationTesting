#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : ful01.py
# @Author  : CHIN
# @Time    : 2021-01-23

from flask import make_response,jsonify,Flask
from flask_restful import Resource,Api,reqparse
from flask_httpauth import HTTPBasicAuth,HTTPDigestAuth

app = Flask(__name__)
api = Api(app=app)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
	if username=='bobo':
		return 'admin'

@auth.error_handler
def authrized():
	return make_response(jsonify({'status':401,'error':'请认证后再访问'}),401)

@app.route('/index')
@auth.login_required()
def index():
	return jsonify(
		{
			"status": 200,
			"msg": "ok",
			"data": {
				'userId': 1001,
				'name': 'bobo',
				'age': 18
			}
		}
	)

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'status':404,'error':'访问页面不存在'}),404)

@app.errorhandler(405)
def not_found(error):
	return make_response(jsonify({'status':405,'error':'该方法只支持GET请求'}),405)

@app.errorhandler(500)
def not_found(error):
	return make_response(jsonify({'status':500,'error':'请耐心等待，服务正在修复中'}),500)

# @app.route('/login',methods=['POST'])
# def login():
# 	parser = reqparse.RequestParser()
# 	parser.add_argument('username',type=str,help='账号不能为空',required=True)
# 	parser.add_argument('password', type=str, help='密码不能为空')
# 	parser.add_argument('age',type=int)
# 	return jsonify({'status':0,'msg':'ok','data':parser.parse_args()})

# class LoginView(Resource):
# 	def get(self):
# 		return jsonify({'status':0,'msg':'ok','data':''})
#
# 	def post(self):
# 		parser = reqparse.RequestParser()
# 		parser.add_argument('username', type=str, help='账号不能为空', required=True)
# 		parser.add_argument('password', type=str, help='密码不能为空')
# 		parser.add_argument('age', type=int, help='年龄必须是整型')
# 		return jsonify({'status':0,'msg':'ok','data':parser.parse_args()})
#
# api.add_resource(LoginView,'/login',endpoint='login')

if __name__ == '__main__':
    app.run(debug=True)