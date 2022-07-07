#WAp input two number perform calculation based on user input
# add,sub,mul,div...etc
a=int(input('enter a value'))
b=int(input('enter b value'))
choice=input('Enter a choice \n  1.add \n 2.sub\n3.div\n 4.mul\n')
if choice=='add':
    print(a+b)
elif choice=='sub':
    print(a-b)
elif choice=='mul':
    print(a*b)
elif choice=='div':
    print(a/b)
else:
    print('invalid choice')
