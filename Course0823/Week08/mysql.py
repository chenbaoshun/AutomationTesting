#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : mysql.py
# @Author  : Baoshun.Chin
# @Time    : 2020-10-25 12:08
# @Site    : 
# @version : V1.0

# 接口测试连接数据库的目的
# 1.可以读取数据库的关键字段
# 2.case里边，有需要数据mock的情况
# *3.如果可能的话，我们可以在接口测试结束之后。清理掉我们产生的测试数据

import pymysql

class DataBase_tools():
    def __init__(self):
        self.host = '192.168.0.104'
        self.port = 3306
        self.username = 'root'
        self.password = '123456'
        self.database = 'mtx'

        # 建立数据库连接
        self.db = pymysql.connect(self.host, self.username, self.password, self.database, self.port)

    def Select_db(self, Sql):
        self.cursor = self.db.cursor()

        try:
            self.cursor.execute(Sql)
            data = self.cursor.fetchall()
            # print(data)

        except:
            print('select error')

        finally:
            self.cursor.close()

        self.db.close()

        return data

if __name__ == '__main__':
    DB = DataBase_tools()
    data = DB.Select_db("SELECT * FROM `mtx`.`s_goods_spec_value` WHERE `goods_id` = '9'")
    print(data)