#  Gotta have that flash-n-trash
#  please don't dock points for this lol
print('WELCOME TO ROULETTE POCKET LABELER 9000!')

#  First, I'll need to set the value for 'pocket'.

pocket = float(input('Please enter a pocket number: '))

#  Next, lets build our conditions.
#  Even using the elif statements,
#  I think this could have been cleaner.

if pocket == 0:
    print('This pocket is green!')
elif pocket <= 10 and pocket >= 1:
    if (pocket % 2) == 0:
        print('this pocket is Black!')
    else:
        print('this pocket is Red!')
elif pocket <= 18 and pocket >= 11:
    if (pocket % 2) == 0:
        print('this pocket is Red!')
    else:
        print('this pocket is Black!')
elif pocket <= 28 and pocket >= 19:
    if (pocket % 2) == 0:
        print('this pocket is Black!')
#  This is where I realized my colors were reversed...

    else:
        print('this pocket is Red!')
elif pocket <= 36 and pocket >= 29:
    if (pocket % 2) == 0:
        print('this pocket is Red!')
    else:
        print('this pocket is Black!')
#  I got to here before realizing that
#  I was using > and < instead of >= and <=...

elif pocket > 36 or pocket < 0:
    print('Error:Invalid pocket number.')
    print("Are you sure we're looking at the same board here?")
    
#  also, I would have liked to add some kind of loop, so I wouldn't
#  have to keep running the program to check my answers.

print('Goodbye!')

#  I find it comedic how abruptly the program
#  says 'Goodbye!' after printing the color lol.



































































#  is anyone here?
    
