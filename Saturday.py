from datetime import datetime

class Saturday:
    def __init__(self,name,age):
        self.name= 'Sospeter'
        self.age = age 

    def age_calculator(self):
        YOB = 2022-self.age
        print (YOB)
Sat = Saturday('John',90) 
print(Sat.age_calculator())
