class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,other):
        return Vector(self.x + other.x,self.y + other.y,self.z + other.z)

    def __str__(self):
        return f"{self.__dict__}"       # 通过字典的形式输出

def main():
    v1 = Vector(1,1,4)
    v2 = Vector(5,1,4)
    print(v1 + v2)

if __name__ == "__main__":
    main()

