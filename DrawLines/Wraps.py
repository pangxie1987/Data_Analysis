#-*- coding:utf-8 -*-

import logging as log
import time
from functools import wraps

log.basicConfig(level=log.INFO, format='[%(asctime)s] %(message)s')

def methd(func):
    def wrapped(*args,**kwargs):
        return '<i>'+func()+'</i>'
    return wrapped


def add_log(log):
    def detector(func):
        @wraps(func)
        def wrapped(*args,**kwargs):
            log.info('Before %s() call on' % (func.__name__))
            r=func(*args,**kwargs)
            log.info('Arfter %s() call on' % (func.__name__))
            return r
        return wrapped
    return detector

@add_log(log)
def hello():
    print('hello world!')


@add_log(log)
def myfunc(x,y):
    print(x+y)

# hello()
# myfunc(2,3)
# print(myfunc.__name__)

class Animal(object):
    def __init__(self, name):
        self.name = name
    def greet(self):
        print ('Hello, I am %s.' % self.name)

class Dog(Animal):
    def greet(self):
        print ('WangWang.., I am %s.' % self.name)

class Cat(Animal):
    def greet(self):
        print ('MiaoMiao.., I am %s' % self.name)

def hello(animal):
    animal.greet()


# cat=Cat('cat')
#
# hello(cat)

import array
import os
# for root,dir,files in os.walk('C:\WorkDay\Code\Python\Data_Analysis\Doc'):
#     print(root)
#     print(dir)
#     print(files)
#print(os.name)

import requests
import json
#
# pay_load={'page':1,'per_page':10}
#
# headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
#                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
#
# r=requests.post('http://httpbin.org/post',data=json.dumps(pay_load),headers=headers)
#
# # 请求头结构体
# print(r.request.headers)
#
# time.sleep(1)
# print('-'*90)
# #响应报文正文
# print(r.text)
# time.sleep(1)
# print('-'*90)
# # 响应头结构体
# print(r.headers)
#
# print(r.status_code)

# from datetime import datetime
# print(datetime.now())
# print(datetime.utcnow())

import click
#
# @click.command()
# @click.option('--count',default=1,help='Numbers of Greetings')
# @click.option('--name',prompt='Your name',help='The Person to greet')
#
# def hello(count,name):
#     for x in range(count):
#         print('Hello %s'%name)
# hello()

@click.command()
@click.password_option()

def passwd(password):
    click.echo('password:%s'%password)

passwd()