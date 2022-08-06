"""
This is a program that tests on fibonacci.
Happy coding.

"""

fib1=1
fib2=1
fibmax=eval(input('Enter the number to find fibonnacci:'))
count=0
print('',fib1)
print('',fib2)
while count<fibmax:
    fib3=fib1+fib2
    print('',fib3)
    fib1=fib2
    fib2=fib3
    fib3=fib2+fib3
    count= count+1

"""
Positive steps!!

"""