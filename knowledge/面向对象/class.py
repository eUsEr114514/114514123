'''
没有构造函数的类
定义在类下的变量叫：类变量
'''
class Student1:
    name = None
    age = None
    height = None

    def output(self):
        print("学生1的名字叫：",self.name)
        print("学生1的年龄为：",self.age)
        print("学生1的身高为：",self.height)


student_first = Student1()       # 把类实例化
student_first.name = "夂曜欣"
student_first.age = 16
student_first.height = 165
student_first.output()



'''
有构造函数的类
定义在构造函数下的变量加：实例变量 or 成员变量
'''
class Student2:
    def __init__(self,name,age,height):
        self.name = name        # 变量前加上self，可以在整个类中使用，通过self.来获取
        self.age = age
        self.height = height

    def __str__(self):
        return "学生2的名字叫：" + self.name + "."


# 实例化时直接把参数的值放进去，构造函数会被调用 ↓
student_second = Student2("叶晗涵",16,163)
print(student_second)


