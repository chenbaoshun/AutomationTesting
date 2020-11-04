#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: Add_cartApi.py
# @Author: Bull
# ---
# 知识点：使用基类，编写一个接口的封装
from day8.api.Base_Req import Base_Reg


class Add_castApi(Base_Reg):
    #假如这个接口的头信息是特殊的，需要重写
    def __init__(self):
        self.headers = {'Content - Type':'application / json',
                        'charset' : 'utf-8',
                        'X-Requested-With': 'XMLHttpRequest'
                        }
        self.ip = 'http://121.42.15.146:9090'

    def add_cart(self):
        url = '/mtx/index.php?s=/index/cart/save.html'
        data = {'goods_id': 4, 'stock': 1}
        resp = self.post_trmplate(url,data)
        return resp


if __name__ == '__main__':
    req = Add_castApi()
    res = req.add_cart()
    print(res.json())