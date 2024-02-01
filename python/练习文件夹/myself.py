# open(__file__,"a").write(open(__file__).read())
# 上面的代码为追加写入自身文件

lines = 1
def run():                      # 定义一个计算代码行数的函数
    global lines
    len = lines
    for i in range(len):
        lines = lines + lines

run() # 2           （第一次运行代码后的代码行数）
run() # 8           （第二次运行代码后的代码行数）
run() # 2048        （第三次运行代码后的代码行数）
run() # 6 x 10 ^ 620 （约等于）

print(f"第四次运行后的代码行数为：{lines}行")



