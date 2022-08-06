num = eval(input('Enter a number: '))

for a in range (1,num-1):
    factor = num * a
    print(factor ,'',sep='---', end = '')
    if a ==num-1:
        print(factor ,'', end = '')
        break
     