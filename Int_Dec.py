num = eval(input('Enter any decimal number: '))

int_part = int(num)
decim_part = num - int(num)

print('The number = ',num)
print('\nThe integer part = ',int_part)
# to format a floating point number, we use te syntax 
#       {:.xf}.format(number)
#       where:
#               x = the number of decimal places required.
print('\nThe decimal part = {:.6f}'.format(decim_part))