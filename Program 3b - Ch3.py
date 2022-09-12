#gotta have that welcome message!
print('==================== Fast Freight Shipping Co ====================')
print('============================ FastCalc ============================')

# First, we get some handcrafted user input.
w = float(input('Please enter the weight of the package to be sent(in pounds): '))
if w <= 2:
    print('At a rate of $1.50 per pound, your total is $',format(w * 1.5, '.2f'))
elif w > 2 and w <= 6 :
    print('At a rate of $3.00 per pound, your total is $',format(w * 3, '.2f'))
elif w > 6 and w <= 10:
    print('At a rate of $4.00 per pound, your total is $',format(w * 4, '.2f'))
elif w > 10:
    print('At a rate of $4.75 per pound, your total is $',format(w * 4.75, '.2f'))


print('=========================== Thank You! ===========================')

