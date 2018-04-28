# -*- coding:utf-8 -*-
'''
python Decorator（装饰器）
'''

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

import time
from functools import wraps

# 装饰器
def timethis(func):
    @wraps(func)
    def Wraps(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(func.__name__,end-start)
        return result
    return Wraps

        
@timethis
def counttime(n):
    while n>0:
        n-=1

counttime(100000)


'''
__getattr__
实例调用属性时，访问到不存在的属性会调用__getattr__
'''
class ClassA(object):
    def __init__(self,classname):
        self.classname=classname

    def __getattr__(self,attr):
        return('invoke_getattr',attr)

insA=ClassA('mytest')
#有classname属性，
print(insA.classname)
#__dict__属性，访问类中所有的属性，键为属性名，值为属性值
print(insA.__dict__)
#grade属性没有找到，则调用__getattr__
print(insA.grade)

'''
__getattribute__
实例获取属性时，都是通过调用__getattribute__
'''
class ClassB(object):
    def __init__(self,classname):
        self.classname=classname
    def __getattr__(self,attr):
        return('invote_getattr',attr)
    def __getattribute__(self,attr):
        return('invote_gettattribute',attr)

insB=ClassB('ClassB')
print(insB.classname)
print(insB.__dict__)
print(insB.grade)


'''
__setattr__
通过实例对属性进行赋值时，会调用__setattr__
'''

class ClassC(object):
    def __init__(self,classname):
        self.classname=classname

insC=ClassC('ClassC')

print(insC.__dict__)
# 调用自带的__dict__ 增加属性
insC.tag='tag'
print(insC.__dict__)


class student(object):
    '''
    定义一个类时实现了__call__函数，这个类型就成为可调用的
    换句话说 把这个类的对象当做函数用
    '''
    def __init__(self,name):
        self.name=name
    def __call__(self):
        print('my name is %s'%(self.name))

    def sayhello(self):
        print('hello my name is %s'%(self.name))

st=student('pitt')
st.sayhello()
st()


class Dict(dict):
    '''
    通过__setattr__  __getattr__   __delattr__重写dict
    '''

    def __setattr__(self,key,value):
        print("In __setattr__")
        self[key]=value

    def __getattr__(self,key):
        try:
            print("In __getattr__")
            return (self[key])
        except KeyError as k:
            return None
    
    def __delattr__(self,key):
        try:
            del self[key]
        except KeyError as k:
            return None

    def __call__(self,key):
        '''
        __call__用于实例自身的调用，相当于()的功能
        '''
        try:
            print('In __call__')
            return self[key]
        except KeyError as k:
            return("In __call__ Erorr")

s=Dict()
print(s.__dict__)

s.name='hello'
# 由于调用的__setattr__ name属性没有加到__dict__
print(s.__dict__)
# 调用__call__
print(s('name'))
# dict默认行为  
print(s['name'])
# __getattr__
print(s.name)

# __delattr__
del s.name
print(s('name'))


'''
classmethod
类不需要实例化  可以直接调用下面的方法
'''
class CCC(object):
    @classmethod
    def hello(self):
        print('hello')

CCC.hello()


'''
Decorator  
'''

def salesgirls(discount):
    def serve(func):
        def Wraps(*args):
            print('hello,what size do you want?',func.__name__)
            result=func(*args)
            
            if result:
                print('OK glad to hear,and this one is %s%% off'%discount)
            else:
                print('there will be other shirt')
            return result
        return Wraps
    return serve


@salesgirls(50)
def try_this_shirt(size):
    print('i want %s size'%size)
    if size<=35:
        print("it's too small")
        return False
    else:
        print('just OK')
        return True

result=try_this_shirt(36)
print('Mum：Do you want to buy this ?',result)


'''
class 的Decorator方法
'''

class MyDecorator(object):
    def __init__(self,func):
        print('In MyDecorator __init__')
        self.func=func
    def __call__(self):
        self.func()
        print('In MyDecorator __call__')

@MyDecorator
def functions():
    print('In functions')

print('FInished the class!')
# 注意执行顺序
functions()
