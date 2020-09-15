#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File:20200830_蓝佳莉_第三周作业.py
# @Author: lanjiali
# ---
# -*- coding: utf-8 -*-

# 原需求：
# 工作之中，会需要注册大量的账户（需要注册信息，姓名、身份证、地址）。这时候编辑和记录名字就成为一个问题。
# 这里编写批量随机生成姓名函数

# 作业1.对批量生成随机姓名函数，进行优化。要求写入文件的数据没有重复项

#思路：1.导入随机数函数，实现随机
#2.定义一个生成单个随机名字的函数
#3.定义批量生成随机名字的函数
#4.定义写入函数：
    # ①设置随机生成的随机名字的个数
    # ②调用批量生成随机名字函数
    # ③批量随机生成名字去重
    # ④批量写入

import random           #导入随机数函数的模块

def get_random_name():    #定义一个生成一个随机名字的函数
    '''
    随机生成一个名字
    :return: fname返回随机的姓；lname返回随机的名
    '''
    first_name = ['赵','钱','孙','李','周','吴','郑','王','冯','陈','欧阳','费','贺','薛','严','雷','万','夏','姚','陆','汤']
    last_name = ["承恩","承瀚","宇翔","冠廷","冠宇","柏翰","彦廷","柏宇","宥廷","柏睿"]
    # 使用random.choice(seq)函数，直接选择列表中的随机一项
    fname = random.choice(first_name)
    lname = random.choice(last_name)
    name = fname+lname
    return name

def get_random_names(num):
    '''
    批量生成随机名字的函数
    :param num: 随机生成名字的个数
    :return:
    '''
    name_list = []          #存储多个名字的列表变量
    for i in range(num):    #传入随机生成几个名字就循环几次
        name = get_random_name()
        name_list.append(name)
    #print(name_list)
    return name_list

def write_random_names():
    '''
    去重写入随机生成的批量随机名字
    :return:
    '''
    num = int(input('请输入要随机生成随机名字的个数：')) #输入一个数值确认随机生成名字的个数
    name_list=get_random_names(num)                #调用批量生成随机名字的函数
    removename_list = []                           #设置一个空列表存储去重后的名字
    print(name_list)
    f = open('names.txt','a')
    for i in name_list:                            #先把随机生成的名字列表去重
        if i not in removename_list:               #如果名字不在新列表中，则添加到新列表里
            removename_list.append(i)
    print(removename_list)

    for i in  removename_list:                     #把去重后的名字写入names.txt，只保证单次写入无重复项
        #print(i)
        f.write(i)
        f.write('\n')
    f.close()

if __name__ == '__main__':#主函数调用
    write_random_names()

# 2.按照面向对象的思想，尝试设计一个随机生成地址的“类”（进行语言描述即可，不用具体编码）
# 思路：地址的属性有以下几点：
# 1.地址的国家
# 2.地址的城市
# 3.地址的区/县
# 4.地址的街道
# 5.地址的详细地址
# 6.利用随机模块拼接地址，定义随机一个生成地址函数


class address():#地址的属性
    addr_country = ['中国','英国','法国','俄罗斯']
    addr_city = ['北京','上海','广州','深圳','成都','武汉','重庆']
    addr_county = ['江北区','朝阳区','东城区','海淀区','昌平区','大兴区','西城区']
    addr_street = ['xx街道','a街道','b街道','c街道']
    addr_details_address = ['花园小区','绿园小区','红苹果小区','橙子小区']

    def random_address(self):#随机生成地址的函数
        country = random.choice(address.addr_country)
        city = random.choice(address.addr_city)
        county = random.choice(address.addr_county)
        street = random.choice(address.addr_street)
        details_addr = random.choice(address.addr_details_address)
        addr =country+city+county+street+details_addr
        return addr

random_addr =address() #调用address类
print(random_addr.random_address())