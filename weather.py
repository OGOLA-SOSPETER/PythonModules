Hours='morning', 'afternoon', 'evening'
time =eval(input('Enter the time of day: '))
if time >6 and time <12:
    print('Good Morning')
elif time>12 and time<16:
    print('Good Afternoon..')
elif time>16 and time<=24:
    print('Good Evening.')
else:
    print('Invalid!!!')

print('Loop terminated..')

    