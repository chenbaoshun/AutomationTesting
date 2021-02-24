#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
# @File    : oop1.py
# @Author  : CHIN
# @Time    : 2020-12-26 20:22

'''
类：是由一系列属性相同的

'''

class F1(object):
	pass

'''
对象的创建 --> 就是类实例化的过程
三个特性：
1. 对象的句柄 --> 区分不同的对象
f2 = F1()
f1 = F1()
print(id(f1))
print(id(f2))

2. 属性
	公有属性：public
		类属性
		实例属性
		局部属性
	私有属性：private
3. 方法
'''

'''类属性和实例属性的案例代码'''
# class Person(object):
# 	# 共同点：类属性
# 	gongTong = 'China'
# 	def __init__(self,name,age):		# 构造函数，初始化类
# 		# 实例属性
# 		self.name = name
# 		self.age = age
# 		# zone = '空间'
#
# 	def getNmae(self):
# 		return self.name
#
# 	def getAge(self):
# 		return self.age
#
# 	def setName(self,name):
# 		self.name = name
#
# 	def setAge(self,age):
# 		self.age = age
#
# 	def info(self):
# 		return 'name:{0},age:{1},address:{2}'.format(self.getNmae(),self.age,self.gongTong)
#
# per = Person('chin',18)
# per2 = Person('lisi',20)
#
# per2.setName('lisa')
# per2.setAge(29)
#
# print(per2.info())

# class Person(object):
# 	def __init__(self,*args,**kwargs):
# 		self.args = args
# 		self.kwargs = kwargs
#
# 	def userInfo(self):
# 		# print(self.kwargs.values())
# 		print(self.args)

# per1 = Person(name='chin')
# per1.userInfo()
#
# per2 = Person(name='chin',age=18)
# per2.userInfo()
#
# per3 = Person(name='chin',age=18,ismarry='marryed')
# per3.userInfo()

# per4 = Person('chin',19,'chengdu')
# per4.userInfo()

'''
首先一个类，不管是否写了构造函数，都是有构造函数的
构造函数:
1.初始化属性
'''
# class Person(object):
# 	def __init__(self,name,age):
# 		self.name = name
# 		self.age = age


# class Person(object):
# 	@property
# 	def getUserID(self):
# 		pass
#
# per = Person()
# per.getUserID()


'''
静态方法:直接使用类名来进行调用，它属于类
对象也可以调用静态方法，但是一般不建议这样做
'''
# class MySQL(object):
# 	@staticmethod
# 	def conn(user):
# 		pass

# MySQL.conn('admin')
# per = MySQL()
# per.conn('admin')


'''
类方法：直接使用类来进行调用，属于类
'''

# class Person(object):
# 	@classmethod
# 	def conn(cls):
# 		pass
#
# Person.conn()

'''
继承：重用已经存在的数据和行为，减少代码的重复编写
子类继承父类所有的实例变量和方法
'''

'''类属性的继承'''
# class Person(object):
# 	china = 'earth'
#
# class ChiPerson(Person):
# 	pass
#
# per = ChiPerson()
# per.china

# 子类由于业务需求，需要继承父类的实例属性
# class Fruit(object):
# 	def __init__(self,name):
# 		self.name = name
#
# class Apple(Fruit):
# 	def __init__(self,name,type,color):
# 		super(Apple,self).__init__(name)
# 		# Fruit.__init__(self,name)
# 		self.type = type
# 		self.color = color
#
# 	def info(self):
# 		print('名称：{0}，种类：{1}，颜色：{2}'.format(self.name,self.type,self.color))
#
# apple = Apple('苹果','种类','红色')
# apple.info()

# 子类由于业务需求，不需要继承父类的实例属性
# class Fruit(object):
# 	def __init__(self,name):
# 		self.name = name
#
# class Apple(Fruit):
# 	def __init__(self,type,color):
# 		self.type = type
# 		self.color = color
#
# 	def info(self):
# 		print('种类：{0}，颜色：{1}'.format(self.type,self.color))
#
# apple = Apple('种类','红色')
# apple.info()

'''
构造函数 --> 钩子函数
方法的继承:
1.子类为什么要重写父类的方法：子类有自己的特性
当子类重写了父类的方法后，对子类进行实例化后，子类调用的方法（父类，子类都存在），执行的方法是子类的方法

单个类继承的原则：
1.从上到下：子类继承了父类，但是子类没有重写父类的方法，那么子类实例化后，调用的方法是直接调用父类当中的方法
2.从下到上：子类继承了父类，但是子类没有重写父类的方法，那么子类实例化后，调用的方法是子类当中的方法（子类优先考虑自己类的方法）
'''
# class Fruit(object):
# 	def eat(self):
# 		print('水果可以吃')
#
# class ChiApple(Fruit):
# 	def __init__(self,color):
# 		self.color = color
#
# 	def eat(self):
# 		print('颜色变{0}的时候就可以吃'.format(self.color))
#
# class UsaApple(ChiApple):
# 	def eat(self):
# 		print('我是USA的苹果')
#
# # apple = Apple('红色')
# apple = UsaApple('颜色')
# apple.eat()

# class Person(object):
# 	def __init__(self,name):
# 		self.name = name
#
# 	def info(self):
# 		print(self.name)
#
# class Son(Person):
# 	def __init__(self,name,age,address):
# 		Person.__init__(self,name)
# 		self.age = age
# 		self.address = address
#
# 	def info(self):
# 		print(self.name)
#
# s = Son('name')
# s.info()

'''
多个类的继承：从左到右的原则
'''
class Person(object):
	def eat(self):
		print('人要吃饭')

class Mother(Person):
	def eat(self):
		print('喜欢吃菜')

class Father(Person):
	def eat(self):
		print('喜欢吃馍')

class Child(Father,Mother):
	pass

child = Child()
child.eat()