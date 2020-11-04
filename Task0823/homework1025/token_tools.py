#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : token_tools.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-10-26 23:47
# @Site    : 
# @version : V1.0

import time
import base64
import hmac

def generate_token(key, expire=3600):
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode('utf-8')
    sha1_ts_hexstr = hmac.new(key.encode('utf-8'), ts_byte, 'sha1').hexdigest()
    token = ts_str + ':' + sha1_ts_hexstr
    b64_token = base64.urlsafe_b64encode(token.encode('utf-8'))
    return b64_token.decode('utf-8')

def certify_token(key, token):
    token_str = base64.urlsafe_b64decode(token).decode('utf-8')
    token_list = token_str.split(':')
    if len(token_list) != 2:
        return False
    ts_str = token_list[0]
    if float(ts_str) < time.time():
        return False
    know_sha1_tsstr = token_list[1]
    sha1 = hmac.new(key.encode('utf-8'), ts_str.encode('utf-8'), 'sha1')
    calc_sha1_tsstr = sha1.hexdigest()
    if calc_sha1_tsstr != know_sha1_tsstr:
        return False
    return True