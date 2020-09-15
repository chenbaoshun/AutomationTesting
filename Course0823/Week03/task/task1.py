#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : task1.py
# @Author  : Baoshun.Chin
# @Time    : 2020-09-08 21:21
# @Site    : 
# @version : V1.0

# import random
# import string
# import time
#
# def random_name():
#     xing = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛' \
#            '奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康' \
#            '伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董梁杜阮蓝闵' \
#            '席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯昝管卢莫经房裘缪干解应宗' \
#            '丁宣贲邓郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁荀羊於惠甄曲家封芮羿储靳汲邴糜松井段富巫' \
#            '乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘钭厉戎祖武符刘景詹束龙叶幸司韶郜黎蓟薄' \
#            '印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙池乔阴鬱胥能苍双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍卻璩桑桂' \
#            '濮牛寿通边扈燕冀郏浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘' \
#            '匡国文寇广禄阙东欧殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空曾毋沙乜养鞠须丰巢关蒯相' \
#            '查后荆红游竺权逯盖益桓公万俟司马上官欧阳夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳' \
#            '淳于单于太叔申屠公孙仲孙轩辕令狐钟离宇文长孙慕容鲜于闾丘司徒司空丌官司寇仉督子车颛孙端木' \
#            '巫马公西漆雕乐正壤驷公良拓跋夹谷宰父谷梁晋楚闫法汝鄢涂钦段干百里东郭南门呼延归海羊舌微生' \
#            '岳帅缑亢况郈有琴梁丘左丘东门西门商牟佘佴伯赏南宫墨哈谯笪年爱阳佟第五言福'
#     ming = '伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清' \
#            '飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善' \
#            '厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家' \
#            '致树炎德行时泰盛秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环' \
#            '雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶' \
#            '怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑筠柔竹霭凝晓欢霄枫芸菲寒欣滢伊亚宜可姬舒影荔枝思丽秀' \
#            '飘育馥琦晶妍茜秋珊莎锦黛青倩婷宁蓓纨苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希'
#     X=random.choice(xing)
#     M="".join(random.choice(ming) for i in range(2))
#     name = X+M
#     return name
#
# if __name__ == "__main__":
#     i = range(1,10)
#     for u in i:
#         time.sleep(1)
#         name = random_name()
#         print(name)

# chars = 'sdffggghhjj'
#
# l = "".join(random.choice(chars) for i in range(2))
# print(l)
# # 大约可以解释成：
# I = []
# for i in range(2):
#     I.append(random.choice(chars))
#
# print("N".center(120, "*"))
# print(I)

# def 函数(参数):
#     '''
#     函数说明
#     :param 参数:
#     :return:
#     '''
#     代码1
#     代码2
#     ......

#encoding=utf-8

# import random
#
# def randomMac():
#     macstring = "0123456789abcdef"*12
#     macstringlist=random.sample(macstring,12)
#     return "{0[0]}{0[1]}:{0[2]}{0[3]}:{0[4]}{0[5]}:{0[6]}{0[7]}:{0[8]}{0[9]}:{0[10]}{0[11]}".format(macstringlist)
# print(randomMac())
#
# def randomIP():
#     a = random.sample(range(1,256),4)
#     b = map(str,a)
#     return '.'.join(b)
# print(randomIP())

# class LentError(Exception):
#     def __init__(self,lenth,min_lenth):
#         self.lenth = lenth
#         self.min_lenth= min_lenth
#     def __str__(self):
#         return f'长度异常:长度为{self.lenth}，不够最小长度{self.min_lenth}'
#
# def main():
#     try:
#         password = input('请输入密码:')
#         if len(password)< 8:
#             raise LentError(len(password),8)
#     except Exception as e:
#         print(e)
#     else:
#         print('长度满足最小8位，密码输入完成')
#
# main()

import time
try:
    f = open('test.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        print('意外终止了读取数据')
    finally:
        f.close()
        print('关闭文件')
except:
    print('没有这个文件')


import random

def get_random_name():      # 随机生成姓名方法
    first_name = ['赵','钱','孙','李','周','吴','郑','王','冯','陈','褚','卫','蒋','沈','韩','杨','张','李','左丘','西门','南宫','令狐']
    last_name = ['豫','章','故','郡','洪','都','新','府','星','分','翼','轸','地','接','衡','庐','襟','三','江','','而','带','五','湖','控','蛮','荆','而','引','瓯','越','物','华','天','宝','龙','光','射','牛','斗','之','墟','人','杰','地','灵','徐','孺','饯','子']

    fname = random.choice(first_name)       # 随机生成姓
    lname = "".join(random.choice(last_name) for i in range(2))     # 随机生成名（1到2位）

    fullname = fname + lname

    return fullname

# file = open('name_data.txt','w')
# def get_random_names(num):
#     for i in range(num):
#         name = get_random_name()
#         file.writelines(name)
#         # file.write('\n')
#     return name
#
# count = int(input('请输入生成姓名数量：'))
# get_random_names(count)
# file.close()

def write_data_t(data):     # 写入数据方法
    with open('name_data.txt','a+') as fp:      # 追加写入，也可单独写入
        fp.writelines(data)
        fp.write('\n')
        fp.close()