#(1)AEIRHMETIC OPERATOR(+(add),-(sub),*(mul),/(division),%(modulus),**(exponent or power),//(floor division))
a=20
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)  #it will give quotient part in float
print(a%b)  #it will give the remainder part
print(a**b) #(exponent)a to the power (a^b)
print(a//b) #(floor division)it will give quotient part in integer only
print("*****")
#2 
c=12
d=6
print(c/d) #2.0
print(c//d) #2
#3
print("____")
c=12.0
d=6
print(c/d) #2.0
print(c//d) #2.0
print("------")
#4
name='priti'
print(name*4) #here we will get 4 yimrd priti
#6
print("------")
name='priti'
print(name+'254') #here priti is a string and  254 is also a string
#8
print("___---____")
a,b,c,d,e,f,g,h=1,2,3,4,5,6,7,8
result=(a+b)*(c+d)*e**f//g+h
print(result)
#7
print("------")
name='priti'
print(name+254) #here we will get an error bcz priti is a string and 254 is a number
#5
print("------")
name='priti'
print(name*5.5) # here we will get an error bcs we can use here only integer value
