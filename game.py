import math
from re import A
from xml.etree.ElementInclude import include



"""
This is a game for children

"""
from random import randint

num1=randint(1,10)
num2=randint(1,10)
prod1=num1*num2
p=0
for p in range (30):
    num1=randint(1,10)
    num2=randint(1,10)
    prod1=num1*num2
    prod=0
    a=0
    print('Question', p ,' : ',num1,' * ', num2, ' =  _____?' )
    a=eval(input('Enter value: ')) #prod1
    if(a==randint(1,10) and randint(1,10)==prod1):
        print('Congratulations!! \n You are a wit...')
    else:
        print('You cannot disapprove the checker!!!!! \n The correct answer = ', prod1)

    p=p+1
    