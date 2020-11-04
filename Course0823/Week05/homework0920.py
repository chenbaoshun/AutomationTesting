#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : homework.py
# @Author  : Baoshun.Chin
# @Time    : 2020-09-20 09:34
# @Site    : 
# @version : V1.0

'''
一、作业：
1.对“学生管理系统.py”进行调试和理解
    # 目的
    # 1.适应修改别人代码的场景
    # 2.栗子里主要使用了“封装”思想
    # 3.复习基本数据类型
2.当前的删除学员信息（del_student），并没有删除掉数据文件中的数据。考虑如何优化（提示：文件保存的时候，'w'模式会覆盖写入）
    # 思路解析：
    # 首先接收键盘输入的“学好”
    # 删除“字典”对象
3.考虑异常处理，例如：
“增加学生时，数据重复”
“删除学生时，没有找到删除项”
“显示数据时，没有数据的情况”等……
'''

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
    def __init__(self,id,name,score):       #绑定在实例化开始
        self.id = id
        self.name = name
        self.score = score
        # print(f'{id},{name},{score}')

    def __str__(self):      #绑定在print一个实例的实际
        return (f'{self.id},{self.name},{self.score}')
# student = Student(1,'东坡',100)

class Manager():
    students_dict = {}      #用来储存操作数据
    # 0.处理键盘输入的方法
    def set_up(self):
        def menu():
            print('*'*10+'欢迎使用“学生管理系统”'+'*'*10)
            print('1.添加学生')
            print('2.显示信息')
            print('3.删除学生')
            print('0.退出系统')     #在系统退出时进行文件保存
            print('*'*40)

        # 读取txt文件到students_dict变量
        self.load_file()        #进入系统选项之前，先进行文件读取
        while True:
            menu()      #展示提示信息
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
        stu_id = input('请输入学号:')
        stu_name = input('请输入姓名:')
        stu_score = input('请输入分数:')

       # 把字典添加到列表中
        if stu_id in self.students_dict.keys():
            print("学号已存在，请重新输入")
            return

        student = Student(stu_id,stu_name,stu_score)
        self.students_dict[stu_id] = student        #学生对象
        print(self.students_dict.values())
        print("添加成功")

    # 2.显示信息方法
    def show_all_info(self):
        if len(self.students_dict) <= 0:
            print('系统还没有学生信息，请添加~')     # 如果为空，则提示
            return
        print('*'*40)
        print('学号 | 姓名 | 分数')
        for student in self.students_dict.values():
            id = student.id
            name = student.name
            score = student.score
            print(f'{id} | {name} | {score}')

    # 3.删除学员信息方法
    def del_student(self):
        del_id = input('请输入要删除的学号:')

        if del_id not in self.students_dict.keys():
            print('删除失败，系统中没有该学生，请确认后再次删除~\n')
            return
        else:
            del self.students_dict[del_id]
            print('删除成功！！！\n')

        # result = self.remove_stu_by_uid(del_id)
        # if result == 0:
        #     print("删除失败,请确认后再次删除！")
        # elif result == 1:
        #     print("{}删除成功".format(del_id))
        # if del_id in self.students_dict.values():
        #     del self.students_dict[del_id]
        # else:
        #     print("没有该学生，请再次确认后进行删除操作！")

    def remove_stu_by_uid(self, uid):
        # 判断请求删除信息是否存在字典里
        if uid in self.students_dict:
            # 如果存在则删除
            del self.students_dict[uid]
            return 1
        # 如果走到这一步，说明请求信息不存在字典里
        return 0

    # 保持数据到文本中
    def save_text(self):
        with open("stu_data.txt","w",encoding="UTF-8") as w:
            for student in self.students_dict.values():     # 遍历学生信息字典内的值
                if student:     # 如果有值，就写入文件内
                    w.write(str(student)+'\n')
                else:
                    break
        # f = open('stu_data.txt', "a+", encoding="UTF-8")        #初步决定使用a+模式
        # for student in self.students_dict.values():
        #     f.write(str(student)+'\n')
        w.close()

    # 从文件中加载数据
    def load_file(self):
        with open("stu_data.txt", "r", encoding="UTF-8") as r:
        # 思路：进行按行的读取，
        # 每一行使用','进行分割
        # 在把取出的元素，装到students_dict
        #     for line in r.readlines():
        #         student_info = line.split(',')
        #         id = student_info[0]
        #         name = student_info[1]
        #         score = student_info[2]
        #         student = Student(id,name,score)
        #         self.students_dict[id] = student
            while True:
                data = r.readline()
                if data:
                    data_split = data.split(",")
                    stu = Student(data_split[0],data_split[1],data_split[2].rstrip("\n"))
                    self.students_dict[data_split[0]] = stu
                else:
                    break
        r.close()

def main():
    obj = Manager()
    obj.set_up()

if __name__ == '__main__':
    main()
