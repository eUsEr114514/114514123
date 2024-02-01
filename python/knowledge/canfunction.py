'''
字符串函数----------------------------------------------------------------------------------------
'''
#join为一个字符串列表和另一个字符串进行分隔
print(" and ".join(["you","me"]))
#输出you and me

#split与join相反，把带有字符串分隔的字符串转换为列表
print("you,me".split(","))
#输出['you', 'me']

#replace为替代另一个字符串中的子字符串
print("hello python".replace("python","world"))
#输出hello world

#startswith和endswith分别检测字符串首尾是否有子字符串
string_Boolean = "I like Minecraft"
print(string_Boolean.startswith("i"))
#输出False
print(string_Boolean.endswith("Minecraft"))
#输出True

#upper和lower分别为更改字符串大小写
print("hello world".upper())
print("MINECRAFT".lower())
#把整段字符串改为大写或小写输出

'''
数值函数-----------------------------------------------------------------------------------------
'''
print(max(1,5,3,7,5,9,3))       #输出该组数列中的最大数字
print(min([0,2,5,7,4,8,3]))       #输出该组列表中的最小数字
print(abs(-75))                 #输出一个数的绝对值
print(sum([i for i in range(101)]))     #输出列表的综合* * * * * * * * * （重要）

'''
列表函数-------------------------------------------------------------------------------------------
'''
list = [11,45,14]
if all([i > 10 for i in list]):             #如果列表里的所有数字都大于10才继续执行以下语句
    print("list列表里的全部数字都大于10")
if any([i % 5 for i in list]):              #如果列表里的有数字可以整除5就可以继续执行以下语句
    print("list列表里有数字可以整除5")

for i in enumerate(list):       #enumerate枚举函数可用于同时便利列表的索引和值
    print(i)


