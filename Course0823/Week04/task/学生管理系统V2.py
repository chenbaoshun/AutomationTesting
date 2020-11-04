#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : 学生管理系统V2.py
# @Author  : Baoshun.Chin
# @Time    : 2020-09-16 23:14
# @Site    : 
# @version : V1.0

class ControlPanel(object):
    """控制面板类"""
    def __init__(self):
        """初始化属性方法"""
        # 初始化数据管理类
        self.dm = DataManager()

    def start_up(self):
        """系统运行的方法"""
        while True:
            # 调用信息展示页面
            self.show_menu()
            # 获取相应操作的信息
            ipt = input("请输入执行的信息:")
            # 获取到的值，如果为零则退出循环，及退出系统
            if ipt == '0':
                break
            # 获取到的值如果不为零，则调用相应的方法
            self.handle_command(ipt)
        # 在退出系统前，保存数据到相应的文件内
        self.dm.save_to_file()

    def show_menu(self):
        """展示详情信息页面"""
        print("*" * 30)
        print("1、添加学生信息")
        print("2、删除学生信息")
        print("3、查找学生信息")
        print("4、更改学生信息")
        print("5、显示所有学生信息")
        print("0、退出系统")
        print("*" * 30)

    def handle_command(self, ipt):
        """根据用户输入的信息进行相应的操作"""
        if ipt == '1':
            # 添加学生信息
            self.add_student()
        elif ipt == '2':
            # 删除学生信息
            self.remove_student()
        elif ipt == '3':
            # 查找学生信息
            self.find_student()
        elif ipt == '4':
            # 更改学生信息
            self.modify_student()
        elif ipt == '5':
            # 显示所有学生信息
            self.show_all_student()
        else:
            print("输入有误请重新输入")

    def add_student(self):
        """添加学生信息的方法"""
        # 获取需要存储的信息
        ipt_uid = input("请输入学号:")
        ipt_name = input("请输入姓名:")
        ipt_age = input("请输入年龄:")
        # 创建学生类的对象
        stu = Student(ipt_uid, ipt_name, ipt_age)
        # 将学生对象对位键值对的值存入字典中
        result = self.dm.add_one_student(stu)
        if result == 0:
            print("添加失败")
        elif result == 1:
            print("添加成功")

    def show_all_student(self):
        """显示全部学生信息的方法"""
        # 调用数据管理类里面的方法，并得到返回值（返回值为数据对象的引用）
        stus = self.dm.get_all_student()
        # 遍历数据对象的引用，打印的时候制动调用Student类里面的__str__方法
        for item in stus:
            print(item)

    def find_student(self):
        """查找指定学生信息的方法"""
        # 获取需要查找信息的学号
        ipt_uid = input("请输入查找学生的学号:")
        # 获取返回对象的引用
        stus = self.dm.find_stu_by_uid(ipt_uid)
        print(stus)

    def remove_student(self):
        """删除指定学生信息的方法"""
        # 获取需要删除信息的学号
        ipt_uid = input("请输入需要删除信息的学号:")
        # 调用数据管理类的删除方法
        result = self.dm.remove_stu_by_uid(ipt_uid)
        # 判断返回值来确认信息是否删除
        if result == 0:
            print("删除失败")
        elif result == 1:
            print("删除成功")

    def modify_student(self):
        """修改指定学生信息的方法"""
        # 获取需要修改信息的学号
        ipt_uid = input("请输需要修改信息的学号")
        # 调用数据操作里面修改方法
        stu = self.dm.modify_stu(ipt_uid)
        if stu == 0:
            print("修改失败")
        # 获取需要修改的信息
        stu.uid = input("请输入新的学号:")
        stu.name = input("请输入新的姓名:")
        stu.age = input("请输入新的年龄:")
        print("修改成功")


class DataManager(object):
    """数据管理类"""
    def __init__(self):
        """初始化属性方法"""
        self.students = {}
        self.load_from_file()

    def add_one_student(self, stu):
        """接收控制面板端传来的信息，并添加学生信息到字典里"""
        # 判断请求添加的数据是否已经存在
        if stu.uid in self.students:
            return 0
        # 如果未存在，则添加到字典里
        self.students[stu.uid] = stu
        return 1

    def get_all_student(self):
        """当控制面板调用此方法时，返回数据对象的引用"""
        return self.students.values()

    def find_stu_by_uid(self, uid):
        """遍历学生字典信息，匹配到相应的引用对象返回"""
        for key, value in self.students.items():
            if uid == key:
                return value
        return 0

    def remove_stu_by_uid(self, uid):
        # 判断请求删除信息是否存在字典里
        if uid in self.students:
            # 如果存在则删除
            del self.students[uid]
            return 1
        # 如果走到这一步，说明请求信息不存在字典里
        return 0

    def modify_stu(self, uid):
        # 查找请求信息是否在字典里
        for key,value in self.students.items():
            # 如果有相应的信息则返回对应引用
            if key == uid:
                return value
        # 如果走到这一步则说明请求信息不存在字典里
        return 0

    def load_from_file(self):
        """在控制面板里初始化数据管理类时，开始加载文件内的数据"""
        with open("stu_data.txt","r") as f:
            # 循环取值
            while True:
                data = f.readline()
                # 每次取到的值，都进行相应的处理，将数据的对象引用存入字典里
                if data:
                    # 将得到的数据用","分隔开
                    data_split = data.split(",")
                    # 建立学生信息对象（最后的rstrip("\n")作用是，去除字符串最右边的"\n"）
                    stu = Student(data_split[0], data_split[1], data_split[2].rstrip("\n"))
                    # 将数据对象的引用存入字典内
                    self.students[data_split[0]] = stu
                else:
                    break


    def save_to_file(self):
        """将数据保存到指定文件内"""
        # 获取文件操作对象W
        with open("stu_data.txt","w") as w:
            # 遍历学生信息字典内的值
            for value in self.students.values():
                # 如果有值，就写入文件内
                if value:
                    # 使用字符串拼接将数据存入文件内
                    w.write(value.uid+","+value.name+","+value.age+"\n")
                else:
                    break


class Student(object):
    """创建学生类"""
    def __init__(self, uid, name, age):
        """初始化属性对象"""
        self.uid = uid
        self.name = name
        self.age = age

    def __str__(self):
        """调用学生的实例对象时自动调用此方法"""
        return "学号:%s，姓名:%s，年龄:%s" % (self.uid, self.name, self.age)


def main():
    """学生管理系统的主函数"""
    # 创建实例对象
    con = ControlPanel()
    # 调用实例方法开始运行程序
    con.start_up()


if __name__ == '__main__':
    main()