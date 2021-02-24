#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_book.py
# @Author  : CHIN
# @Time    : 2021-01-30

from base.method import Requests
from common.public import *
from tools.operateYaml import OperationYaml
from tools.operateExcel import OperateExcel
import pytest
import json

class TestBook:
	excel = OperateExcel()
	obj = Requests()

	def result(self,r,row):
		assert r.status_code==200
		assert self.excel.getExpect(row=row) in json.dumps(r.json(),ensure_ascii=False)

	def test_book_001(self):
		'''
		获取所有书籍的信息
		:return:
		'''
		r = self.obj.get(url=self.excel.getUrl(row=1))
		self.result(r=r,row=1)

	def test_book_002(self):
		'''
		添加书籍
		:return:
		'''
		r = self.obj.post(url=self.excel.getUrl(row=2),json=self.excel.getJson(row=2))
		# print(r.json())
		bookID = r.json()[0]['datas']['id']
		writeContent(content=bookID)

	def test_book_003(self):
		'''
		查看添加的书籍
		:return:
		'''
		r = self.obj.get(url=self.excel.getUrl(row=3))
		self.result(r=r,row=3)

	def test_book_004(self):
		'''
		编辑书籍
		:return:
		'''
		r = self.obj.put(url=self.excel.getUrl(row=4),json=self.excel.getJson(row=4))
		self.result(r=r,row=4)

	def test_book_005(self):
		'''
		删除书籍
		:return:
		'''
		r = self.obj.delete(url=self.excel.getUrl(row=5))
		self.result(r=r,row=5)


if __name__ == '__main__':
    pytest.main(["-s", "-v", "test_book.py", "--alluredir", "../report/book_report/result"])
    import subprocess

    subprocess.call('allure generate ../report/book_report/result/ -o ../report/book_report/html --clean', shell=True)
    subprocess.call('allure open -h 127.0.0.1 -p  8088 ../report/book_report/html', shell=True)