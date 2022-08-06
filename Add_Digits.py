# A python program that accepts a number.,
#The program then finds the sum of the digits in the number and returns the result.

#input
nums = input('Enter the number: ')
#getting individual digits
num = str(nums)
#length of digits
num_len = len(nums)

#summation
summ = 0
for a in range(num_len):
    summ = summ + int(num[a])

#display
print ('The sum of the digits in the number : ',nums, ' = ',summ)