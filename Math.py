
#import libraries
from math import *
from random import randint
from decimal import Decimal
#a = 5
#b = 7
for x in range(50):
    #finding the random numbers
    a = randint(1,100)
    b = randint(1,100)
    print('-'*30)
    print ('a = ',a)
    print ('b = ',b)
    print('The GCD of ',a,' and ',b,' = ',gcd(a,b))
    print('The LCM of ',a, 'and ',b, ' = ',lcm(a,b))
#printing the maximum and the minimum 
    print('The maximum between the two numbers = ',max(a,b))
    print('The minimum number = ',min(a,b))
    print('Using decimal notation to divide = {:.4f}'.format(Decimal(a)/Decimal(b)))


#formatting a number to have the commas after three digits
print('{:,d}'.format(200098878676680))