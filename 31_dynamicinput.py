#dynamic input
#1 without typecast output
print("withot typecasting")
a=input('enter a')
b=input('enter b')
c=a+b
print(c)
#let a=10 ,b=28 here we will get output as 1028   by default it take the a and b value as string so we need to type cast here
#2 with type cast to int
print("with typecasting to int")
a=int(input('enter a'))
b=int(input('enter b'))
c=a+b
print(c)
#3 type cast to float
print("with typecasting to float")
a=float(input('enter a'))
b=float(input('enter b'))
c=a+b
print(c) 
print(type(c))
#4 string type (type cast not required)
print("in string typecasting is not required")
username=input('enter u r username')
print(username)
print(type(username))
# here it is string so type casting is not required 
#5 typecast to complex 
print("with typecasting to complex")
a=complex(input('enter a' ))
b=complex(input('enter b'))
c=a+b
print(c) 
