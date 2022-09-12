#  Exercise 14: Compound Loan Calculator
print('=========CompLoanCalc v1.0=========')
print('===Please enter the values below===')

#  Storing inputs

p = float(input('Principal amount: '))
r = float(input('Interest rate: '))
t = float(input('Number of years:  '))
n = float(input('Amount of times per year the interest is compounded: '))

#Convert rate

r = r/100


#  Calculate the input.
#  I had to modify the formula for the math to come out correctly.
#  I was getting terribly large numbers otherwise (which would make for a great program to give me some more money lol)

a = p * pow(1+(r/n), n*t)


#  Display result. This one was giving me troubles.
#  After hours of syntax errors, I somehow fixed two problems at once.

print('Projected account balance: %.2f' %a)
