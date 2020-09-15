#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: 函数练习.py
# @Author: Bull
# ---
# 需求：
# 工作之中，会需要注册大量的账户（需要注册信息，姓名、身份证、地址）。这时候编辑和记录名字就成为一个问题。
# 这里编写一个随机生成姓名函数

# 需求分析：
# 1.编写一个函数，我可以命名为"get_random_name()"
# 2.针对“大量”这个描述，我可以理解为。函数需要具有批量的功能，所以在"get_random_name()"
# 的基础上。拓展编写"get_random_names()"批量生成的函数
# 3.对于需求里边的，生成什么样的姓名。需要先搞清楚。
# 这里，我们要做的是生成中文姓名

# 具体设计
# 1.利用python的random库（官方文档地址： https://docs.python.org/zh-cn/3/library/random.html），来实现“随机”的功能
# 2.对于姓名，一般我们会分成“姓氏” 和 “名字”
# 3.所谓的随机姓名，可以设计成 随机姓氏 + 随机名字（随机的量=姓氏*名字）

# 编码

import random
# v = random.randint(1,5)
# print(v)

def get_random_name():
    first_name = ['赵','钱','孙','李','周','吴','谭','上官','欧阳','费','贺','薛','严','雷','万','白','夏','姚','陆','汤']
    last_name = ["承恩","承瀚","宇翔","冠廷","冠宇","柏翰","彦廷","柏宇","宥廷","柏睿"]
    #思路1：
    # 利用随机数字 + 列表的“下标”
    # random.randint('随机数字的起始值'，'随机数字的结束值')，它会返回一个范围内的随机整数
    # 列表的len()函数，正好可以获得列表元素的数量
    # range_f_name = len(first_name)-1
    # range_l_name = len(last_name)-1
    #
    # fname = random.randint(0,range_f_name)
    # lname = random.randint(0, range_l_name)
    #
    # res = first_name[fname] + last_name[lname]
    #
    # 练习1：
    # 用random.choice(seq)来替换randint,优化上述代码
    # 思路2：
    # 使用random.choice(seq)函数，直接选择列表中的随机一项
    fname = random.choice(first_name)
    lname = random.choice(last_name)
    res = fname + lname
    return res

# name = get_random_name()
# print(name)

# 练习2：
# 利用get_random_name()方法，
# 扩展编写get_random_names()#批量生成随机姓名函数

#针对业务复杂的需求，可以考虑拆分模块来完成函数
def get_random_names(num):#批量生成随机姓名
    name_list = []
    for i in range(num):
        name = get_random_name()
        name_list.append(name)
        print(name_list)
    return name_list

# get_random_names(9)


