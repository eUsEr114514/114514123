'''
继承：
子类继承父类，子类拥有父类的全部属性
多态：
子类继承父类，子类拥有不同于父类的属性
'''
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def test(self):
        print("父类中的test")

class BoyStudent(Student):
    def test(self):                 # 在子类中重新编写父类函数（重写）
        super().test()              # super函数可以调用父类中的函数
        print("boy子类中的test")

class GirlStudent(Student):
    def test(self):
        print("girl子类中的test")

girl_student_first = GirlStudent("夂曜欣",16)  # 实例化girl子类
print(girl_student_first.name)
girl_student_first.test()                               # 执行girl子类中重新编写父类的test函数








