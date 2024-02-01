'''
with open("text1.mcfunction",'+a',encoding='utf-8')as file:
    for i in range(100):
        command = "setblock ~{0} ~ ~".format(i)
        file.write(command + '\n')

with open("text1.mcfunction",'w')as file:
    for i in range(100):
        command = "particleex tickparameter endRod ~ ~2 ~{0} 0 1 1 1 240 0 0 0 -10 10 x=t;y=sin(t) 0.1 10 1000".format(i)
        file.write(command + '\n')

with open("text2.mcfunction",'w')as file:
    for i in range(88):
        command = "setblock -399.5 75 -{0} minecraft:sea_lantern".format(i + 1850)
        file.write(command + '\n')
        
with open("text3.mcfunction",'w')as file:
    for i in range(88):
        command = "setblock -412.5 75 -{0} minecraft:sea_lantern".format(i + 1850)
        file.write(command + '\n')
'''

# import math
# sins = 1
# sinss = math.asin(sins)
# print(sinss)

# num = 0
# while True:
#     num += 1
#     print(f"还是PVP大佬{num}")
#     if num == 2 ** 31 - 1:
#         break

# string = "是"
# pvp = input("你是PVP大佬吗")
# if pvp == string:
#     print("恭喜你通过面试")
# else:
#     print("抱歉!你不适合我们GRW团队")

def f():
    print("f")
    return g
def g():
    print("g")
    return f

f()()()()()