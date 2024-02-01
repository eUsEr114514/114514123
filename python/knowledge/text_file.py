#文本分析器
def string_count(text,letter):                  #定义一个字符串计数函数，变量为text和letter
    count = 0                                   #设置初始计数值为0
    for i in text:                              #使用for循环遍历text变量并赋值给i
        if i == letter:                         #条件判断，如果i等于变量letter
            count = count + 1                   #计数值+1
    return count                                #返回计数值(切记一定要指定返回区域，否则将返回None)

while True:
    print("输入1可查看文件里的文本")
    print("输入2可查看文件里的文本中某些字母的出现次数")
    
    print("输入0可退出服务")
    chose = int(input("请选择你想要的服务："))
    if chose == 0:
        break
    elif chose != 1 and chose != 2:
        print("抱歉，没有这项服务")
        continue
    filename = input("请输入文件名：")
    with open(filename)as file:                 #读取文件
        text = file.read()
        if chose == 1:
            print(text)
        elif chose == 2:
            letter = input("请输入想要查询的字母")
            print(string_count(text,letter))
        













close_window = input("click enter")