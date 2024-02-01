class Information:
    def __init__(self,name,student_id,age):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.scores = {"Chinese":0,"Math":0,"English":0}
    
    def add_score(self,cource,score):
        if cource in self.scores:
            self.scores[cource] = score

    def print_all(self):
        print(f"该学生的姓名为:{self.name},学号为:{self.student_id},年龄为:{self.age},成绩为:")
        for cource in self.scores:
            print(f"{cource}:{self.scores[cource]}分")

electron = Information("电子","114514","16")
electron.add_score("Chinese",114)
electron.add_score("Math",150)
electron.add_score("English",114)
electron.print_all()



