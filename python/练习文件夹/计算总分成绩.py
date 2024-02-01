#计算你的六科总分（纯分数，不赋分）
Chinese = int(input("请输入你的语文成绩："))
Math = int(input("请输入你的数学成绩："))
English = int(input("请输入你的英语成绩："))
Physics = int(input("请输入你的物理成绩："))
Chemistry = int(input("请输入你的化学成绩："))
Geography = int(input("请输入你的地理成绩："))
score_result = Chinese + Math + English + Physics + Chemistry + Geography
print(f"你的总分成绩为：{score_result}")
close_window = input("按Enter关闭窗口")