#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_mysql.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-06 22:11
# @Site    : 
# @version : V1.0

import pytest
import pymysql

@pytest.fixture()
def connSQL():
    conn = pymysql.connect(host='localhost',user='root',passwd='123456',db='db')
    return conn

def closeSQL(connSQL):
    connSQL.close()

@pytest.fixture()
def init(connSQL):
    connSQL
    yield
    closeSQL(connSQL)

def test_get_one(init,connSQL):
    cursor = connSQL.cursor()
    cursor.execute('select * from user;')
    print(cursor.fetchall())