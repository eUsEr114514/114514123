'''
十进制转二进制————————————————————————————————————————————
decimalism十进制
binary_system二进制
十进制转二进制用bin
'''
decimalism = 114514
binary_system = bin(decimalism)
print(binary_system)

'''
lambda表达式——————————————————————————————————————
def func(x,y):
    return x + y
等同于
var = lambda x,y : x + y    
'''
var = lambda num1,num2 : num1 + num2
print(var(7,5))

'''
比较列表内的数字大小用sorted方法(sort排序)
'''
list = [11,45,14]
sort = sorted(list)
print(sort)

'''
打印乘法口诀表
'''
for i in range(1,10):
    print()
    for j in range(1,i + 1):
        print(f"{i} x {j} = {i * j} ")

'''
水仙花数：一个三位数，它的每一位数的立方加起来等于这个三位数
获取一个三位数中的每一位数的值
num = 750
single = num % 10                个位数：除于10取余数
tens = (num % 100) // 10       十位数：处于100取余数，然后除于10取整数
entenary = num // 100              百位数：除于100取整数
'''
for i in range(100,1000):
    single = i % 10
    tens = (i % 100) // 10
    centenary = i // 100
    if single ** 3 + tens ** 3 + centenary ** 3 == i:
        print(i)







