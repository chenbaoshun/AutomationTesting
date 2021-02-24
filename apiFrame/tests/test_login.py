#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : test_login.py
# @Author  : CHIN
# @Time    : 2021-01-16

import pytest
import json
import allure
from base.method import Requests
from common.public import filePath
from tools.operateYaml import OperationYaml

obj = Requests()
objYaml = OperationYaml()

@allure.story("接口测试")
@pytest.mark.parametrize('data', objYaml.readYaml())
def test_login(data):
    r = obj.post(
        url = data['url'],
        json = data['data']
    )

    assert data['expect'] in json.dumps(r.json(),ensure_ascii=False)

if __name__ == '__main__':
    pytest.main(["-s", "-v", "test_login.py", "--alluredir", "../report/result"])
    import subprocess

    subprocess.call('allure generate ../report/result/ -o ../report/html --clean', shell=True)
    subprocess.call('allure open -h 127.0.0.1 -p  8088 ../report/html', shell=True)