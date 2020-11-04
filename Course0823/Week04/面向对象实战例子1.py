#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: 面向对象实战例子1.py
# @Author: Bull
# ---
# 初始需求：一个随机生成地址的类
import random

class address:
    District = {"北京市": "", "上海市": "", "天津市": "", "重庆市": "",
                "河北省": ["石家庄市", "唐山市"] }
    def get_random_address(self):
        # print(type(District))
        Province = random.choice(list(self.District))
        tmp = Province
        if self.District[tmp] == "":
            return (tmp)
        address = tmp+random.choice(self.District[tmp])
        return (address)

# obj = address()
# var = obj.get_random_address()
# print(var)

# 新需求：要求生成只“河北省”的地址
# 思路：使用继承
class HeBei_address(address):#从父类继承 ①储存地址的“字典”对象 ②随机组合数据的放啊
    District = {"河北省": ["石家庄市", "唐山市","秦皇岛市",'邯郸市','邢台市','保定市','廊坊市']}

obj = HeBei_address()
var = obj.get_random_address()
print(var)

# 新需求:要求批量生成地址数据
class batch_address(address):
    def batch(self,n=10):
        res_list=[]
        for i in range(n):
            temp = self.get_random_address()
            res_list.append(temp)
        return res_list