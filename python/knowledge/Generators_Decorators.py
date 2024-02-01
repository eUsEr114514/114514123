#Generators生成器，需要调用时才生成
list = (i for i in range(10))       #用小括号
#用next方法获取：next(list)

#一个函数使用了yield，这个函数就是一个生成器
def Generators():
    x = 7
    while x > 5:
        #print(x)
        x = x - 1
        yield x

for i in Generators():
    print(i)

#Decorators装饰器，装饰器是在不修改目标函数代码的前提下，为目标函数新增功能的函数
def decorators(func):                        #定义装饰器
    def wrap():
        print("===============")
        func()                               #把下面的函数f()作为参数放进decorators函数中，在这一行被调用
        print("===============")
    return wrap

@decorators                                  #用@调用装饰器
def f():
    print("hello world")
f()
'''
输出结果:
===============
hello world
===============
'''

