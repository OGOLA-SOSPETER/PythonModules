# Printing of palindrome numbers
# A palindrome is a number that is the same wheteher read from the right or from the left.

for a in range(1000):
    #assigning the palindrome numbers to the integer as a string
    pal = str(a)
    # test case
    if pal == pal [: : -1]:
        #output
        print(pal)