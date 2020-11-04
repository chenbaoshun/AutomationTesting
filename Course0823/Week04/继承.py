#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: 继承.py
# @Author: Bull
# ---

# class A:
#     def __init__(self):
#         self.num = 1
#     def info_print(self):
#         print('基础类输出文本')
#         print(self.num)
#
# # 假说这个类完成以后，有新的需求。
# class B(A):
#     name = 'obj_b'          #类属性
#     # ②也可以更新父类的方法 或者 属性
#     def __init__(self):
#         self.num = 100      #init方法里定义的叫“实例属性”
#     # 如果继承了父类的子类 ， 要写代码有几种情况
#     # ①写和父类完全不相关的
#     def obj_b_print(self):
#         print(self.name)
#
#
# son = B()
# son.info_print()
# son.obj_b_print()

# 关于子类"重写"
class Teacher(object):
    def __init__(self):
        self.name ="麻辣大师"
        self.kongfu = "‘独门绝技’"
    def make_food(self):
        print(f'{self.name}开始做菜')
        print(f'用{self.kongfu}做出麻辣香锅')

    def func1(self):
        pass

    def func2(self):
        pass

class Student(Teacher):
    def __init__(self):
        self.kongfu = "‘独门绝技’"
        self.name = "‘麻辣学徒’"
        self.stu_kongfu = "‘最炫绝技’"

    def stu_make_food(self):
        print(f'申请专利的{self.stu_kongfu}麻辣香锅')


# obj = Teacher()
# obj.make_food()

student = Student()
student.make_food()#徒弟用师傅传授的原装“独门绝技”做的食物

student.stu_make_food() #徒弟用自创的方法做饭