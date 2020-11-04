#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: 多态的实现.py
# @Author: Bull
# ---
#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: 继承.py
# @Author: Bull
# ---
# class Teacher(object):
#     def __init__(self):
#         self.name ="麻辣大师"
#         self.kongfu = "‘独门绝技’"
#     def make_food(self):
#         print(f'{self.name}开始做菜')
#         print(f'用{self.kongfu}做出麻辣香锅')
#
# class Student(Teacher):
#     # pass
#     def make_food(self):
#         print('徒弟开始，照猫画虎')
#         print(f'用{self.name}的{self.kongfu}做出麻辣香锅')
#
# teacher = Teacher()
# teacher.make_food()
#
# print('*'*40)
# # ==========
# obj = Student()
# obj.make_food()

# 多态的具体编写
# 1.单纯实现“同名函数”
# 这个例子里，我认为只要有Quack()这个方法 那么这个类就属于“Duck鸭子类”
# class Duck():#鸭子类
#     def Quack(self):  #鸭子叫的方法
#         print('呱呱')
#
# class Swan():#天鹅类
#     def Quack(self):
#         print('鹅鹅')
#
# class Plane():                                 # 飞机类
#     def Quack(self):
#         print("隆隆隆")
#
# class Dog():
#     def wang(self):
#         print('汪汪汪')
#
# def Quake(object):          #这个函数是我预期可以成功运行的，前提就是接受到的object具有一个Quack()方法
#     object.Quack()

# duck = Duck()
# place = Plane()
# swan = Swan()
# Quake(duck)
# Quake(place)
# Quake(swan)
#
# 这是一个反例，传入的对象里边没有Quake()方法。就会报错
# dog = Dog()
# Quake(dog)

#多态在python里边的实现方式是“实现同名函数”


# 2.通过“继承”实现多态（更简单快捷）
# class Dog():
#     text = '喜欢溜达'
#     def play(self):
#         print(self.text)
#
# class Lily_dog(Dog):
#     text = '喜欢在商城溜达'
#     # 通过继承，得到了Dog类的 pyay()方法
#
# class TomDog(Dog):
#     text = '喜欢在公园溜达'
#     # 通过继承，得到了Dog类的 pyay()方法
#
# class play():
#     def play_with_dog(self,object):
#         object.play()
#
# lily_dog = Lily_dog()
# dog = Dog()
# tom_Dog = TomDog()
#
# obj_play = play()
# obj_play.play_with_dog(dog)
# obj_play.play_with_dog(tom_Dog)
# obj_play.play_with_dog(lily_dog)

