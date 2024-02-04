a=float(input('enter the 1st no.'))

print('''1: addition
      2:subtraction
      3:multiplication
      4:division''')
choice=int(input('enter the choice'))
b=float(input('enter the 2nd no.'))

if choice==1:
    Output=a+b
    print('the Output is',Output)
elif choice==2:
    Output=a-b
    print('the Output is',Output)
elif choice==3:
    Output=a*b
    print('the Output is',Output)
elif choice==4:
    Output=a%b
    print('the Output is',Output)
else:
    print('enter valid choice')
