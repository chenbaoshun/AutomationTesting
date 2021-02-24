#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : client.py
# @Author  : CHIN
# @Time    : 2021-01-23

import requests
import shutil

def send_request(url):
	r = requests.get(url)
	return r.status_code

def visit_ustack():
	return send_request('http://www.ustack.com')

class Remove(object):
	def rmdir(self, path='c:/log'):
		r = shutil.rmtree(path)
		if r==None:
			return 'success'
		else:
			return 'fail'

	def exist_get_rmdir(self):
		return self.rmdir()