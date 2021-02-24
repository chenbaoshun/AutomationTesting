#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : loginOop.py
# @Author  : Baoshun.Chin
# @Time    : 2020-12-30 20:34
# @Site    : 
# @version : V1.0

'''
需求：
要求注册账号，然后注册的账号登录到系统后，显示出登录的账号昵称
1.模拟注册
2.模拟登陆
3.登录成功后获取昵称的函数
'''

import json

# def inOut():
# 	username = input('请输入账号：\n')
# 	pwd = input('请输入账号密码：\n')
# 	return username,pwd
#
# def register():
# 	'''
# 	实现账号的注册功能
# 	:return:
# 	'''
# 	username,pwd = inOut()
# 	temp = username + '|' + pwd
# 	json.dump(temp,open('login.md','w'))
#
# def login():
# 	'''
# 	实现账号的登录功能
# 	:return:
# 	'''
# 	username, pwd = inOut()
# 	f = str(json.load(open('login.md','r')))
# 	list1 = f.split('|')
# 	if username == list1[0] and pwd == list1[1]:
# 		return True
# 	else:
# 		return False
#
# def getNick(func):
# 	'''
# 	实现获取昵称的功能
# 	:return:
# 	'''
# 	f = str(json.load(open('login.md', 'r')))
# 	list1 = f.split('|')
# 	if func:
# 		print('{0},您好，欢迎你来到coco空间'.format(list1[0]))
# 	else:
# 		print('请登录系统')
#
# def main():
# 	while True:
# 		t = int(input('1.注册 2.登录 3.退出系统\n'))
# 		if t==1:
# 			register()
# 		elif t==2:
# 			getNick(login())
# 		elif t==3:
# 			import sys
# 			sys.exit(1)
# 		else:
# 			print('输入错误，请继续...')
# 			continue
#
# if __name__ == '__main__':
# 	main()
import sys


class Login(object):
    def __init__(self,username,pwd):
        self.username = username
        self.pwd = pwd

    def getUsername(self):
        return self.username

    def setUsername(self,name):
        self.username = name

    def getPwd(self):
        return self.pwd

    def setPwd(self,passwd):
        self.pwd = passwd

    def register(self):
        temp = self.username + '|' + self.pwd
        json.dump(temp, open('login.md', 'w'))
        print('恭喜你，注册成功，请登录！')

    def login(self):
        f = str(json.load(open('login.md', 'r')))
        list1 = f.split('|')
        if self.username == list1[0] and self.pwd == list1[1]:
            return True
        else:
            return False

    def info(self):
        f = str(json.load(open('login.md', 'r')))
        list1 = f.split('|')
        func = self.login()
        if func:
            print('{0},您好，欢迎你来到coco空间'.format(list1[0]))
        else:
            print('请登录系统')

    def exit(self):
        sys.exit(1)


def main():
    per = Login('chin','admin')
    while True:
        try:
            t = int(input('1.注册 2.登录 3.退出系统\n'))
        except Exception as e:
            print(e.args)
        else:
            if t == 1:
                per.register()
            elif t == 2:
                per.info()
            elif t == 3:
                per.exit()
            else:
                print('输入错误，请继续...')
                continue
        finally:
            pass

if __name__ == '__main__':
    main()