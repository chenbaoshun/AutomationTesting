#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : operateExcel.py
# @Author  : CHIN
# @Time    : 2021-01-17

import xlrd
from common.public import *
from tools.operateYaml import OperationYaml

class ExcelVarles:
    caseID = "测试用例编号"
    caseModel="模块"
    caseName="接口名称"
    caseUrl = "请求地址"
    casePre = "前置条件"
    method = "请求方法"
    paramsType = "请求参数类型"
    params="请求参数"
    expect="期望结果"
    isRun="是否运行"
    headers="请求头"
    status_code="状态码"
    # caseID=0
    # des=1
    # url=2
    # method=3
    # data=4
    # expect=5
    #
    # @property
    # def getCaseID(self):
    #     return self.caseID
    #
    # @property
    # def description(self):
    #     return self.des
    #
    # @property
    # def getUrl(self):
    #     return self.url
    #
    # @property
    # def getMethod(self):
    #     return self.method
    #
    # @property
    # def getData(self):
    #     return self.data
    #
    # @property
    # def getExpect(self):
    #     return self.expect

class OperateExcel(OperationYaml):
    def getSheet(self):
        book = xlrd.open_workbook(filePath('data', 'books.xls'))
        return book.sheet_by_index(0)

    # @property
    # def getRows(self):
    #     '''获取总行数'''
    #     return self.getSheet().nrows
    #
    # @property
    # def getCols(self):
    #     '''获取总列数'''
    #     return self.getSheet().ncols
    #
    # def getValue(self,row,col):
    #     return self.getSheet().cell_value(row,col)
    #
    # def getCaseID(self,row):
    #     return self.getValue(row=row,col=ExcelVarles().getCaseID)
    #
    # def getUrl(self,row):
    #     url=self.getValue(row=row, col=ExcelVarles().getUrl)
    #     if '{bookID}' in url:
    #         return str(url).replace('{bookID}',readContent())
    #     else:
    #         return url
    #
    # def getMethod(self,row):
    #     return self.getValue(row=row, col=ExcelVarles().getMethod)
    #
    # def getData(self,row):
    #     return self.getValue(row=row,col=ExcelVarles().getData)
    #
    # def getJson(self,row):
    #     return self.dictYaml()[self.getData(row=row)]
    #
    # def getExpect(self,row):
    #     return self.getValue(row=row, col=ExcelVarles().getExpect)

    @property
    def getExcelDatas(self):
        datas = list()
        title = self.getSheet().row_values(0)
        for row in range(1,self.getSheet().nrows):
            row_values = self.getSheet().row_values(row)
            datas.append(dict(zip(title,row_values)))
        return datas

    def runs(self):
        for item in self.getExcelDatas:
            isRun = item[ExcelVarles.isRun]
            print(isRun)

if __name__ == '__main__':
    obj = OperateExcel()
    # print(obj.getValues(2,ExcelVarles().description()))
    # print(obj.getMethod(row=2))
    # print(obj.getJson(row=2))
    obj.runs()