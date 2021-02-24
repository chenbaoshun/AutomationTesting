#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : operateYaml.py
# @Author  : CHIN
# @Time    : 2021-01-16

import  yaml
from common.public import filePath

class OperationYaml:
	def readYaml(self):
		with open(filePath(fileDir='data',fileName='login.yaml'),'r',encoding='utf-8') as f:
			return list(yaml.safe_load_all(f))

	def dictYaml(self,fileDir='data',fileName='books.yaml'):
		with open(filePath(fileDir=fileDir,fileName=fileName),'r',encoding='utf-8') as f:
			return yaml.safe_load(f)

if __name__ == '__main__':
	obj=OperationYaml()
	# print(obj.readYaml())
	print(obj.dictYaml())