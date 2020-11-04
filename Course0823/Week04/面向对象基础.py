#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: 面向对象基础.py
# @Author: Bull
# ---
# 练习题1
#
# 需求：
#
# - 小明今年18岁，身高1.75，每天早上跑完步，会去吃东西
# - 小美今年17岁，身高1.65，小美不跑步，小美喜欢吃东西
# 考点
# 按照面向对象的思路，对这个需求点进行分析

# 分析：
# 1.两条需求都是描述“人类”
# 2.都有“人名”
# 3.都有“年龄”
# 4.都描述了“身高”
#     5.1小明具有“跑步” 和 “吃东西”两个事物
#     5.2小美具有“吃东西”这个事物
class Person():#人类
    # 类的属性：
    name = '小明'
    age = 19
    heigh = 1.75

    # 类的方法：
    def run(self):
        pass
    def eat(self):
        pass

# 练习2
#
# 需求：
#
# - 一只黄颜色的狗狗叫大黄
# - 看见生人汪汪叫
# - 看见家人摇尾巴

class Dog():
    name = '大黄'         #类属性
    color = 'yellow'
    def shake(self):
        name='类方法里的属性'
        print(f'见到家人，好开心{self.name}')

    def shout(self):
        print('生人勿近')
        print('汪汪汪')

    def main(self,moment):
        if moment == '生人':
            self.shout()
        elif moment == '家人':
            self.shake()

dog = Dog()
#
# print(type(dog))
#
dog.main('家人')



# 问题：
# self什么时候用？
# 1.在类下辖的方法中，必须要有一个self参数
# 2.在类里边，进行（当前这个类的其他方法的）方法调用.必须在方法名前边写一个self.
# 3.在类里边，调用类级别的属性。那么必须加self.