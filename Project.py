"""
#input in lowercase and capitalization of each word

Statem = input('Enter your statement here: ')
Statem_replace = Statem.replace(' '  ,' '.upper())
print(Statem_replace)

"""

#User input and print

Num = eval(input('Enter the number you desire: '))

for i in range(Num):
    print('{:8d}'.format(i))
    print('{:>8s}'.format('i'*3))

"""
print('{:6d}'.format(20))
print('{:6d}'.format(245))
print('{:6d}'.format(29867))
print('{:6d}'.format(23838377))
"""