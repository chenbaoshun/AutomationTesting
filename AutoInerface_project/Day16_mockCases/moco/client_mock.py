#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : client_mock.py
# @Author  : CHIN
# @Time    : 2021-01-23

import requests

def send_web(url):
	r = requests.get(url)
	return r.status_code

def visit_web():
	return send_web('http://www.chinketang.com')
