#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 20200823_2周_陈宝顺.py
# @Author  : 陈宝顺、蓝佳莉
# @Time    : 2020-9-1
# @version : V1.4

'''
一、编码作业：
编写一段代码
1.接收键盘输入的英文短语
2.使用空格、逗号、句号分割短语中的单词
3.统计短语中每个单词，出现的次数(忽略大小写)
4.将结果存储为“字典”
范例：
输入:hello python.Learning Python
输出：{'hello':1,'python':2,'learning':1}
'''

text = input("请输入英文短语（标点符号使用英文格式）：")    #定义变量text用于接收输入的英文短语（标点符号使用英文格式）
word_dic = {}                                        #初始化字典word_dic用于存储短语的单词和出现次数

print("***********方案1***********")
for i in text:			#遍历短语
    if i == ',':		#当短语中出现逗号时替换为空格
        text = text.replace(',',' ')
    elif i == '.':      #当短语中出现句号时替换为空格
        text =text.replace('.',' ')

# print("***********方案2***********")
#
# import string                     #导入string包，需使用string中的punctuation方法
# for p in string.punctuation:
#     text = text.replace(p,' ')    #将短语中的标点符号替换为空格

print('-------------------------------')
print('分别使用空格、逗号、句号分割短语中的单词')
print(text)                            #打印短语，即空格分隔

text_comma = text.replace(' ',',')     #将短语中的空格全部替换为逗号
print(text_comma)                      #打印短语，即逗号分隔

text_point = text.replace(' ','.')     #将短语中的空格全部替换为句号
print(text_point)                      #打印短语，即句号分隔
print('-------------------------------')

text = text.lower()                    #将短语中的所有大写字母转换为小写字母（题意中的忽略大小写）
words = text.split(' ')                #定义列表words，把短语以空格分隔为字符串，存储在words列表

while '' in words:                     #删除列表中空字符（短语中多余的空格和开头、结尾的标点符号）
    words.remove('')

for w in words:                        #遍历列表
    count = words.count(w)             #统计重复次数
    word_dic[w] = count                #key=单词，value=重复的次数，添加到字典，字典中如果key值存在则更新value值，所以生成的字典中key不会重复。

print('将短语中每个单词和出现次数统计为字典：\n',word_dic)