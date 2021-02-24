#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
# @File    : login_test.py
# @Author  : CHIN
# @Time    : 2020-12-22 21:16

'''
1.实现用户注册功能
2.实现用户登录功能
3.实现查看用户信息
'''

def typeusername():
	'''
	实现用户名输入
	:return:
	'''
	username = input('请输入注册用户的账号：\n')
	return username

def typepassword():
	'''
	实现密码输入
	:return:
	'''
	password = input('请输入注册用户的密码:\n')
	return password

def register(username,password):
	'''
	实现用户注册功能
	:param username: 注册账号
	:param password: 注册密码
	:return:
	'''
	temp = username + '|' + password
	with open('user_info.txt','w') as f:
		f.write(temp)
		f.close()

def login(username,password):
	'''
	实现用户登录功能
	:param username: 登录账号
	:param password: 登录密码
	:return:
	'''
	with open('user_info.txt','r') as f:
		for line in f:
			list = line.split('|')
			if list[0]==username and list[1]==password:
				return True
			else:
				return False

def info(func):
	'''
	查看用户信息
	:param func: 登录函数
	:return:
	'''
	with open('user_info.txt','r') as f:
		for line in f:
			list = line.split('|')
	if func:
		print('恭喜{0}进入系统！'.format(list[0]))
	else:
		print('很遗憾，输入的账号或密码错误')

def exit():
	'''
	退出系统
	:return:
	'''
	import sys
	sys.exit(1)

def main():
	'''
	主函数
	:return:
	'''
	while True:
		t = int(input('1.注册 2.登录 3.退出系统\n'))
		if t==1:
			username = typeusername()
			password = typepassword()
			register(username,password)
		elif t==2:
			username = typeusername()
			password = typepassword()
			info(login(username,password))
		elif t==3:
			exit()
		else:
			print('输入错误，请继续...')
			continue

if __name__ == '__main__':
    main()