string ='abcdefghijklmnop'
print ('The initial string = ',string)

string = string.upper()
print('\nThe reversed string to uppercase is ',string)

string = string.count('')
print('\nThe total string count = ',string)
print('\n')

"""
string = string.isalpha()
print ('The output = ',string)
"""
password = input('Enter your password: ')
password = password.lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
numbers = 1 ,2 ,3, 4 ,5 ,6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 ,19, 20 ,21, 22, 23 ,24, 25

print('The encrypted password:')
for a in password:
    if a.isalpha():
        print(numbers[alphabet.index(a)],'', end ='')
    else:
        print('Out of range!!')