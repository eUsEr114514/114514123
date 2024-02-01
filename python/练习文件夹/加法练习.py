from random import randint

print("规则：\n接下来会随机生成200以内的整数加法")
print("默认积分为0，每答对一次积分+1，答错一次积分-1，积分达到10分即可胜利")
chance = 0
while chance < 10:
    try:
        num1 = randint(0,101)
        num2 = randint(0,101)
        result = num1 + num2
        print(f"{num1} + {num2}")
        writer1 = int(input("请输入你的答案："))
        
        if writer1 == result:
            chance = chance + 1
            print(f"恭喜你对了，积分+1，你目前的积分为{chance}，还差{10 - chance}个积分就可以获得胜利了哟，加油！")
        else:
            chance = chance - 1
            print(f"错啦，答案是{result}，积分-1，你目前的积分为{chance}，还差{10 - chance}个积分才可以获得胜利，再接再厉")
    except:
        print("错误，输入的不是整数\n已为你重新生成试题")

print("恭喜你获得胜利，奖励一个电子")
close_window = input("按Enter关闭窗口")

