#wap input 3 number chk which one is greatest using if-elif-else
#a=10,b=15,c=12
a=int(input('enter a value'))
b=int(input('enter b value'))
c=int(input('enter c value'))
if a>b and a>c:
    print('a is greatest no. among 3')
elif b>c:
    print('b is greatest no. among 3')
else:
    print('c is greatest no. among 3')