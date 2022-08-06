from math import *
#from math import factorial,floor,pi,ceil,sqrt

num = eval(input('Enter number to find factorial: '))
#finding the factorial of a number
fact_num = factorial(num)

print('The factorial of ',num ,' = ', fact_num)

# more operations on numbers
nums=eval(input('Enter number to operate on: '))
#the floor of numbers
floor_ = floor(nums)
print('The floor of ',nums, ' = ' ,floor_)

#the ceiling of numbers
ceil_ = ceil(nums)
print('The ceil of ',nums, ' = ' ,ceil_)

#the exponential of numbers
exp_ = exp(nums)
print('The exponential of ',nums, ' = ' ,exp_)