# # -*- coding:utf-8 -*-
'''
some test
'''
# import click
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#
#
# @click.command()
# @click.option('--count',default=3,help='bumber of greet')
# @click.option('--name',prompt='Your name',help='the person greet')
# def hello(count,name):
#     for x in range(count):
#         click.echo('hello %s!'%name)
#
# def main():
#     hello()
#
# if __name__=='__main__':
#     main()

#
# import numpy
# import math
#
# def drop_first_last(grades):
#     first, *middle, last = grades
#     print(numpy.mean(middle))
#
# drop_first_last([1,2,3,4,10])
#
# record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
# name,email,*phone=record
#
# print(phone)
#
#
# records = [
#     ('foo', 1, 2),
#     ('bar', 'hello'),
#     ('foo', 3, 4),
# ]
#
# def do_foo(x, y):
#     print('foo', x, y)
#
#
# def do_bar(s):
#     print('bar', s)
#
# for tag, *args in records:
#     print(tag+'\n')
#     if tag == 'foo':
#         do_foo(*args)
#     elif tag == 'bar':
#         do_bar(*args)
#
#
# item=[10,9,8,7,1]
# def sumadd(ddd):
#     head,*tail=ddd
#     #return (sum(tail))
#     print(tail)
#
#     if head:
#         return (head + sum(tail))
#     else:
#         return tail

#print(sumadd(item))


# def fab(max):
#     n, a, b = 0, 0, 1

#     while n < max:
#         # print(b)
#         yield b
#         a,b=b,a+b
#         n=n+1
#         #print(b)

# def fab(max):
#    n, a, b = 0, 0, 1
#    while n < max:
#        print (b)
#        a, b = b, a + b
#        n = n + 1

# for x in (fab(5)):
#     print(x)


# class myyield(object):
#     @staticmethod
#     def Generator():
#         x=range(3)
#         for n in x:
#             print (n)
#
# myyield.Generator()
#
# mylist=(x*x for x in range(3))
# print(mylist)

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

#print(prices.values(),prices.keys())


min_price=(prices.values(),prices.keys())
max_price=max(zip(prices.values(),prices.keys()))

# print(max(zip(prices.items())))
#
#
# for value in (min_price):
#     print(value)
#
# for value in prices.items():
#     print(value)
#
# dict={'a':1,'b':2,'c':3}
#
# print(dict.items())
#
# for value in (dict.items()):
#     print(value)

#print((zip(dict.values(),dict.keys())))
#print(min(prices,key=lambda k:prices[k]))


# for value in ((prices,lambda k:prices[k])):
#     print(value)

#print(min(prices,k='ACME'))

# A = 'hello world'
# print(A)

# import requests

# r = requests.get('http://www.baidu.com')

# print(r.status_code)

# #字符串填充
# List = ['abc','F','ooooo']

# for i in List:
#     print(i.center(20,'*'))
# name = 'pitt'
# n=88
# s = '{name} has {n} messages'
# print (s.format(name='pitt',n=77))

# import os
# print(os.get_terminal_size().columns)
# print(round(2.567,2))
# a=2.1
# b=4.2
# print(a+b)

# from datetime import datetime,timedelta
# import time
# a = datetime(2018,4,24)
# day=timedelta(days=2)
# print(a+day)

# print(a.strftime('%Y-%m-%d'))

# import pickle
# s='hello word'

# data=pickle.dumps(s)
# print(data)
# print(pickle.loads(data))

import csv
import os
from collections import namedtuple

files=os.listdir('.')
# for file in files :
#     print(file)
# with open('apple.csv') as f:
#     f_csv = csv.reader(f)
#     headers = next(f_csv)
#     Row=namedtuple('Row','Open')
#     #print(f_csv)
#     for r in f_csv:
#         row=Row(r)
#         print(row.open)

# with open('apple.csv') as f:
#     f_csv = csv.reader(f)
#     headings = next(f_csv)
#     Row = namedtuple('Row', headings)
#     for r in f_csv:
#         row = Row(*r)
#         print(row.High)


# # 从数据库查询数据 并插入到csv中
# import sqlite3
# import cx_Oracle
# db=cx_Oracle.connect('core/core@10.243.140.152:1521/xe')

# c=db.cursor()


# with open('users.csv','w',encoding='gbk',newline='') as f:
#     f_csv=csv.writer(f)
#     headers=c.execute("select COLUMN_NAME from user_tab_cols where table_name='TB_USER'")
#     f_csv.writerow(headers,)
#     # datas=c.execute('select * from tb_user')
#     # f_csv.writerows(datas)
#     # print('write sucess')

#     for data in c.execute('select * from tb_user'):
#         print (data)
#         f_csv.writerow(data)


# def add (x,y):
#     return x+y

# help(add)

# from urllib.request import urlopen

# def aa(url):
#     def bb(**kwargs):
#         return urlopen(url.format_map(kwargs))
#     return bb

# yahoo = aa('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
# for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
#     print(line.decode('utf-8'))

# class Person():

#     def __init__(self,first_name):
#         self.first_name=first_name

#     @property
#     def first_name(self):
#         return self._first_name

#     @first_name.setter
#     def first_name(self,value):
#         if not isinstance (value,str):
#             raise TypeError('Except a string')
#         self._first_name=value
        
#     @first_name.deleter
#     def first_name(self):
#         raise AttributeError("can't delete attribute")

# person=Person('zhangsan')

# print(person.first_name)


class A(object):
    def __init__(self):
        self.x=0
    def a(self):
        print('I am A')
    def c(self):
        print('I am C')

class B(A):
    def __init__(self):
        # 继承这一个方法
        # super().a()

        # 能继承A这个类下面所有的方法
        super().__init__()
    def a(self):
        print('I am B')

# bb=B()
# # bb.b()
# bb.c()

class AA(object):
    def spam(self):
        print('A.spam')

class BB(AA):
    def spam(self):
        print('B.spam')
        super().spam()  # Call parent spam()

# ins=BB()
# ins.spam()

class Proxy:
    def __init__(self,obj):
        self._obj=obj

    def __getattr__(self,name):
        return getattr(self._obj,name)

    def __setattr__(self,name,value):
        if name.startswith('_'):
            super().__setattr__(name,value)
        else:
            setattr(self._obj,name,value)

# ppp=Proxy('a')

# print(ppp.__dict__)

# print(ppp.name)



# class ClassA(object):
#     def __init__(self,classname):
#         self.classname=classname

#     def __getattr__(self,attr):
#         return('invoke_getattr',attr)

# insA=ClassA('mytest')
# #有classname属性，
# print(insA.classname)
# print(insA.__dict__)
# #grade属性没有找到，则调用__getattr__
# print(insA.grade)



# import time
# from functools import wraps

# # 装饰器
# def timethis(func):
#     @wraps(func)
#     def Wraps(*args,**kwargs):
#         start=time.time()
#         result=func(*args,**kwargs)
#         end=time.time()
#         print(func.__name__,end-start)
#         return result
#     return Wraps

        
# @timethis
# def counttime(n):
#     while n>0:
#         n-=1

# # counttime(100000)

def mydecorator(fn):
    '''
    装饰器
    '''
    def Wraps():
        print('hello i am %s'%fn.__name__)
        fn()
        print('Goodbye %s'%fn.__name__)
    return Wraps

@mydecorator
def foo():
    print('i am foo')

foo()


# def fuck(fn):
#     print ("fuck %s!" % fn.__name__[::-1].upper())
    
  
# @fuck
# def wfg():
#     pass

# # #wfg()