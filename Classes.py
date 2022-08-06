class Student:
    def __init__(self,Name,Age):
        self.Name = Name
        self.Age = Age

    def Display(Name,Age):
        print('You are a student.')
        print('Work hard, ',Name)
        print('You are ',Age,'Years old.')

Std = Student#('Mary',45)
Std.Display('Mary',45)

class Teacher(Student):
    def Display(Name,Age):
        print(Name,Age)

Tr = Teacher
Tr.Display('John',67)