#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : yamlTest.py
# @Author  : Baoshun.Chin
# @Time    : 2021-01-08 21:55
# @Site    : 
# @version : V1.0

import yaml
import pytest
import requests
import json

def readYaml():
    with open('books.yml','r',encoding='utf-8') as f:
        return list(yaml.safe_load_all(f))

@pytest.mark.parametrize("datas",readYaml())
def test_books(datas):
    r = requests.get(url=datas['url'])
    assert datas['expect'] in json.dumps(r.json(),ensure_ascii=False)

if __name__ == '__main__':
    pytest.main(["-s","-v","yamlTest.py"])