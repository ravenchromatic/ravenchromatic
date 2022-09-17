while True:
#  gotta get that INPUT!!!
year = float(input('Enter a year: '))
if year%100 == 0 and year%400 == 0:
    print('In %d February has 29 days' %year)
elif year%100 != 0 and year%4 == 0:
    print('In %d February has 29 days'%year)
else:
    print('In %d February has 28 days'%year)


        
