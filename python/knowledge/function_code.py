#函数程序设计
def twice(func,num):            # 2.把five函数和10分别赋给变量func和num
    return func(func(num))      # 3.返回括号里的func变量赋值为10，并调用five函数
                                # 6.返回括号外的func变量赋值为15，并再次调用five函数
def five(a):                    # 4.把上面的定义函数里的括号里的func为10的变量赋给a变量
    return a + 5                # 5.返回10 + 5 = 15
                                # 7.返回15 + 5 = 20
print(twice(five,10))           # 1.调用twice函数，变量参数为five函数和10
                                # 8.输出20


#纯函数
def pure_function(x,y):
    result = 2 * x + y
    return result / (x + 2 * y)
print(pure_function(7,5))
#不纯函数
list = []
def impure_function(num):
    list.append(num)
    

