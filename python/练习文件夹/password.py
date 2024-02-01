password = "我爱电子"
reply = "谢谢，我也爱你"
chance = 3
surplus = 3
while True:
    surplus = surplus - 1
    inter = input("输入正确密码可查看我想对你说的话:")
    if inter != password:
        print("密码错误，你还剩" + str(chance - 1) + "次机会")
    else:
        print(reply)
        close_window = input("按Enter关闭窗口")
        break
    chance = chance - 1
    if chance == 0:
        print("抱歉，错误次数已达上限，你已无缘查看我想对你说的话")
        close_window = input("按Enter关闭窗口")
        break
        
