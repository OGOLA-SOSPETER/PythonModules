from random import randint

sum = 0
for p in range(50):
    Num = randint(0,100)
    print(Num)
    sum = sum+Num

print('Sum of random numbers = ',sum)