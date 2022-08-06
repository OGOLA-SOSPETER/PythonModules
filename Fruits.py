Fruits  = ['Mango', 'Lemon']
for i in range(len(Fruits)):
    print(Fruits[i])

print('\nAdding additional fruits')
for b in range( 1,5, 1):
    ft = input(' ')
    Fruits[b] = Fruits.append(ft)
    Fruits[b] =  ft

#print(Fruits)


for count in range(len(Fruits)-1):
    print(count,' ',Fruits[count])