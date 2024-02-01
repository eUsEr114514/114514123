# a = float(input("请输入你的a值"))
# b = float(input("请输入你的b值"))
# c = a + b
# print("a + b的值为：" + str(c))

import random
# print(random.randint(0,10))
num = random.randint(0,101)
chance = 5
display_num = 5
while True:
    display_num = display_num - 1
    result = int(input("请输入一个0-100的整数:"))
    if result < num:
        print(f"小了，你还剩{display_num}次机会")
    elif result > num:
        print(f"大了，你还剩{display_num}次机会")
    else:
        print("你真棒！")
        close_window = input("按Enter关闭窗口")
        break
    chance = chance - 1
    if chance == 0:
        print("你的机会已经用完了，不能再继续了")
        close_window = input("按Enter关闭窗口")
        break
    
    



