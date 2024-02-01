def circle():
    print("X^2 + y^2 + Dx +Ey + F = 0")
    print("以上为圆的一般式，输入d，e，f的指将其转换为标准式")
    d = int(input("请输入D的值："))
    e = int(input("请输入E的值："))
    f = int(input("请输入F的值："))
    print(f"圆的标准式为：(x + {d/2}) + (y + {e/2}) = {(d ** 2 + e ** 2 - 4 * f)/4}")

def normal_vector():
    print("输入两个不平行的向量，计算法向量")
    normal1 = input("请输入向量1")
    normal2 = input("请输入向量2")
    



    