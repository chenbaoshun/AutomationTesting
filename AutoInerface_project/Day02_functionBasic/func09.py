#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

# @File    : func09.py
# @Author  : CHIN
# @Time    : 2020-12-22 09:26

'''
函数实战案例
需求：
要求注册账号，然后注册的账号登录到系统后，显示出登录的账号昵称
1.注册的函数
2.登录的函数
3.登录成功后获取昵称的函数
'''

def inOut():
	username = input('请输入账号：\n')
	pwd = input('请输入账号密码：\n')
	return username,pwd
# print(inOut())

def register():
	'''
	实现账号的注册功能
	:return:
	'''
	# username = input('请输入注册账号：\n')
	# pwd = input('请输入账号密码：\n')
	username,pwd = inOut()
	temp = username + '|' + pwd
	with open('login.md','w') as f:
		f.write(temp)
# register()
def login():
	'''
	实现账号的登录功能
	:return:
	'''
	# username = input('请输入登录账号：\n')
	# pwd = input('请输入账号密码：\n')
	username, pwd = inOut()
	with open('login.md','r') as f:
		info = f.read()
	info = info.split('|')
# 	print(info)
# login()
	if username==info[0] and pwd==info[1]:
		return True
	else:
		return False

# print(login())
def getNick(func):
	'''
	实现获取昵称的功能
	:return:
	'''
	with open('login.md','r') as f:
		info = f.read()
	info = info.split('|')
	if func:
		print('{0},您好，欢迎你来到coco空间'.format(info[0]))
	else:
		print('请登录系统')

# getNick(login())

if __name__ == '__main__':
	while True:
		t = int(input('1.注册 2.登录 3.退出系统\n'))
		if t==1:
			register()
		elif t==2:
			getNick(login())
		elif t==3:
			import sys
			sys.exit(1)
		else:
			print('输入错误，请继续...')
			continue