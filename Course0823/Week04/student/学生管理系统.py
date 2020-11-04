#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: 学生管理系统.py
# @Author: Bull
# ---
# 学生管理系统：
# 需要具有
# 1.增加学生信息
# 2.显示信息
# 3.删除学员信息
# 这里的学员信息，主要指3个属性：学号、姓名、分数
# 4.我们的数据，最终要存在txt文件里

# 分析需求：
# 1.学员对象
#     学号属性
#     姓名属性
#     分数属性
# 2.键盘交互对象
    # 1.增加学生信息方法
    # 2.显示信息方法
    # 3.删除学员信息方法
    # 4.处理键盘输入的方法

class Student:
    #定义学生的信息
    def __init__(self,id,name,score):#绑定在实例化开始
        self.id = id
        self.name = name
        self.score = score
        # print(f'{id},{name},{score}')

    def __str__(self):#绑定在print一个实例的实际
        return (f'{self.id},{self.name},{self.score}')
# student = Student(1,'东坡',100)

class Manager():
    students_dict = {}#用来储存操作数据
    # 0.处理键盘输入的方法
    def set_up(self):
        def menu():
            print('*'*40)
            print('欢迎使用“学生管理系统”')
            print('1.添加学生')
            print('2.显示信息')
            print('3.删除学生')
            print('0.退出系统')#在系统退出时进行文件保存

        # 读取txt文件到students_dict变量
        self.load_file()#进入系统选项之前，先进行文件读取
        while True:
            menu()#展示提示信息
            code = int(input('请输入功能的序号:'))
            # 根据序号，连接到不同的功能
            if code == 1:
                self.add_student()
            elif code == 2:
                self.show_all_info()
            elif code == 3:
                self.del_student()
            elif code == 0:
                self.save_text()
                print('退出系统')
                break

    # 1.增加学生信息方法
    def add_student(self):
        id = input('请输入学号:')
        name = input('请输入姓名:')
        score = input('请输入分数:')

        student = Student(id,name,score)
        self.students_dict[id] = student#学生对象
        print(self.students_dict.values())


    # 2.显示信息方法
    def show_all_info(self):
        print('*'*40)
        print('学号==姓名==分数')
        for student in self.students_dict.values():
            id = student.id
            name = student.name
            score = student.score
            print(f'{id}=={name}=={score}')

    # 3.删除学员信息方法
    def del_student(self):
        del_id = input('请输入要删除的学号:')

        del self.students_dict[del_id]

    def save_text(self):

        f = open('data.txt', "a+", encoding="UTF-8")#初步决定使用a+模式
        for student in self.students_dict.values():
            f.write(str(student)+'\n')
        f.close()

    def load_file(self):
        f = open('data.txt', "r", encoding="UTF-8")
        # 思路：进行按行的读取，
        # 每一行使用','进行分割
        # 在把取出的元素，装到students_dict
        for line in f.readlines():
            student_info = line.split(',')
            id = student_info[0]
            name = student_info[1]
            score = student_info[2]
            student = Student(id,name,score)
            self.students_dict[id] = student
        f.close()

obj = Manager()
obj.set_up()

# 目前例子的完成程度：
# 在进入系统的时候会自动读取同目录的data.text
# 在退出系统的时候，会进行数据的保存
# 增加、删除、展示全部、保存数据、读取数据的方法已经初步完成