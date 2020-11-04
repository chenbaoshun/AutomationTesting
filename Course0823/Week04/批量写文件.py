#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: 批量写文件.py
# @Author: Bull
# ---



# 需求：
# 工作之中，会需要注册大量的账户。这时候编辑和记录名字就成为一个问题。
# 这里编写一个随机生成姓名函数

# 分析需求：
# 1.根据功能，方法名称可以定义为“get_random_name”
# 2.需求中描述“大量生成”，可以理解为需要批量功能。继而拓展设计思路，
# 决定实现①生成单个随机名
# 后进行再次包装，编写
# ②生成指定数量随机名
# 两个方法
# 3.题目中没有明确生成什么姓名，需要进一步确定。
# 最终确定生成中文姓名

# 具体设计
# 1.python里有random库（https://docs.python.org/zh-cn/3/library/random.html），
# 它可以随机生成一个数字、或者在列表里随机选择一个item
# 2.中文姓名，可以分为“姓氏”和“名”两部分。
# 3.所谓的随机姓名，可以设计成随机“姓氏”+“名”（姓氏数量*名数量=总随机姓名）。
# 姓氏 和 名字，可以分别储存为一个列表

# 编码：
import random#导入随机包

def get_random_name():#先实现生成单个姓名
    #新建姓名库
    f_name=['赵','钱','孙','李','周','吴','谭','上官','欧阳','费','贺','薛','严','雷','万','白','夏','姚','陆','汤']
    l_name=["承恩","承瀚","宇翔","冠廷","冠宇","柏翰","彦廷","柏宇","宥廷","柏睿"]
    # f_name = ['赵']
    # l_name = ["承恩", "承瀚", "宇翔", "冠廷", "冠宇"]
    # 解决方案1：使用 随机整数+列表下标+拼接字符串
    # random.randint(‘随机起始’，‘随机结束值’) ：return范围内的一个随机整数
    # len(列表)：return列表对象的长度（item数量）
    # range_firstname = len(f_name)-1
    # range_lastname = len(l_name)-1
    #
    # f = random.randint(0,range_firstname)
    # l = random.randint(0,range_lastname)
    #
    # res = (f_name[f] + l_name[l])
    # 解决方案2：使用随机列表值 + 拼接字符串
    f = random.choice(f_name)
    l = random.choice(l_name)
    res = (f + l)


    print("姓名:" + res)

    return res

def batch_name(n=10):
    res_list = []
    for i in range(n):
        temp = get_random_name()
        res_list.append(temp)
        # 遇到新问题，有重名的情况
    # 如果对res_list进行set去重
    return res_list
# 后处理的方案：生成结果集和之后，对结果数据进行“去重”处理

# v = batch_name(4)
# print(v)
# 应对重名的方法：
# 1.使用set去重，将数据从list转换成set。
# 2.使用条件去重+while

def batch_name_v1(n=10):
    res_list = []
    for i in range(n):
        temp = get_random_name()
        #使用while循环+随机生成 解决
        if temp in res_list:                  #只能进行一次结果更新
        # while temp in res_list:             #如果temp（）也就是随机生成的姓名 在结果集和，那就说明这是一个重复的结果
            temp = get_random_name()
        res_list.append(temp)
    return res_list


# 在循环中。只有生成的数据不在结果集的情况下才进行存储，否则继续生成新的数据存到结果集。

def get_write_file(n):                                           # 定义写入文件方法
    # with open('random_name.txt','a',encoding='utf-8') as f:   # 打开文件/关闭文件   'a'追加
    with open('random_name.txt','w',encoding='utf-8') as f:     # 'w'覆盖
        batch_name = batch_name_v1(n)                # 调用随机姓名组合列表方法
        for i in batch_name:                                    # for循环把列表内容写入文件
            f.writelines(i)
            f.writelines('\n')
    return batch_name

get_write_file(4)