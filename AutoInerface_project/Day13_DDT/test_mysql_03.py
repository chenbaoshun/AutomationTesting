#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_mysql_03.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-12 21:19
# @Site    : 
# @version : V1.0

import pymysql

def connMySQL():
    try:
        conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='root',
            db=''
        )
    except Exception as e:
        return e.args
    else:
        cur = conn.cursor()
        # 单个数据的查询
        # sql = 'select * from user where id=%s'
        # params = (1,)
        # cur.execute(sql, params)
        # data = cur.fetchone()
        # print(data)

        # 所有数据的查询
        sql = 'select * from user'
        params = (1,)
        cur.execute(sql, params)
        data = cur.fetchall()
        db = [item for item in data]    # 列表推导式
        print(db)
    finally:
        cur.close()
        conn.close()

# 插入数据
def insertMySQL():
    try:
        conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='root',
            db=''
        )
    except Exception as e:
        return e.args
    else:
        cur = conn.cursor()
        sql = 'insert into user values (%s, %s, %s, %s)'
        # 单条数据
        # params = (3, 'weike', 18, 'chengdu')
        # 多条数据
        params = [
            (4, 'weike', 18, 'chengdu'),
            (5, 'weike', 18, 'chengdu')
        ]
        cur.execute(sql, params)
        conn.commit()
    finally:
        cur.close()
        conn.close()

# 删除数据
def deleteMySQL():
    try:
        conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='root',
            db=''
        )
    except Exception as e:
        return e.args
    else:
        cur = conn.cursor()
        sql = 'delete from user where id=%s'
        # 单条数据
        # params = (3,)
        # 多条数据
        params = [
            (4,),
            (5,)
        ]
        cur.execute(sql, params)
        conn.commit()
    finally:
        cur.close()
        conn.close()


class MySQlHelper():
    def conn(self):
        conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='root',
            db=''
        )
        return conn

    def get_one(self, sql, params):
        cur = self.conn().cursor()
        data = cur.execute(sql, params)
        result = cur.fetchone()
        return result

def checkValid(username, passwd):
    opera = MySQlHelper()
    sql = ''
    params = ''
    result = opera.get_one(sql=sql, params=params)
    if result:
        print('登录成功')