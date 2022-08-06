
                # Multiple operations on strings.

#printing the string count

Name = input('Enter a string: ')

Name1 = Name.count('')



print('The count of the characters in the string = ',Name1-1)

#printing the string 10 times
print('\n')
for a in range(10):
    print(Name)

print('\n')

#printing the first character
Name_index = Name[0]
print('The first character of the string is ',Name_index)

#printing last three characters of string
print('\n')
a = Name.count('')
Last_characs = Name[ a-4: ]
print(' The last three characters are ',Last_characs)

print('\n')

#printing string backwards
Reverse_string = Name[ : : -1]
print(Reverse_string)


print('\n')

#printing the seventh character.
Name_len = Name.count('')
if Name_len >= 7:
    print(Name[6].upper())
else:
    print('The string length is less than 7!!')

print('\n')

#removing the first and last characters of the string
#print(' The string with the first character removed is ',Name[0].remove())


#printing string in caps
Name_caps =  Name.upper()
print(Name_caps)
print('\n')

#replacing a with e

Name_replace =  Name.replace('a', 'e')
print(Name_replace)

print('\n')

#every letter replaced by a *
alpha = 'abcdefghijklmnopqrstuvwxyz'
Name_replace_letter = Name.replace('','*')
print(Name_replace_letter)

