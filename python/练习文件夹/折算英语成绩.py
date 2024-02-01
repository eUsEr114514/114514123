#通过120满分的成绩加上10分听说折算出150满分的成绩
def English_score():
    listen = 10
    writer = int(input("请输入你的英语笔试成绩（120满分）:"))
    result = (writer * 130)/120 + listen
    return result
output = English_score()
print(f"你的英语总分(加上10分听说)为：{output}")
close_window = input("按Enter关闭窗口")