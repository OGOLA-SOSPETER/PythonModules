from math import *
# a program to find the power of 2 to any power
Nos = eval(input('Enter a number: '))
x = pow(2,Nos)
# displaying the last digit of 2
s = fmod(x,10)

#output segment.
print(x)
print(round(s,2))