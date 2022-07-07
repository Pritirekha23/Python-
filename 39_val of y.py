#wap to find out the value of y using
# y(x,n)  ={
   # 1+x= when n=1
   # 1+x/n when n=2
   # 1+x^n when n=3
   # 1+nx when x>3
#}
import math
x=int(input('Enter x value'))
n=int(input('enter n value'))

if n==1:
    y=1+x

elif n==2:
    y=1+( x/n)
    
elif n==3:
    y=1+math.pow(x,n)
    
else:
    y=1+(n*x)

print('y value is',y)