#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

# @File    : port.py
# @Author  : CHIN
# @Time    : 2020-12-20 14:35

import os

def port_is_used(port:str):
    port = str(port)
    command = f"netstat -ano |findstr {port}"
    result = os.system(command)
    print(result)
    # if len(result)>0:
    #     return False
    # else:
    #     return True