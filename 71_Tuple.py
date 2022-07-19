#Tuple--
   # It is immutable(unchangable)
   #it is similar to list data structure . It is a inbuilt data structure .
   #paranthesis  symbol is used to create tuple.
  # u can use as a dictionary key as tuple .
#CREATION OF TUPLE IN DIFFERENT WAY

#1 CREATION of empty tuple
print('empty   tuple creation')
t=()
print(t)
print(type(t))

#2 creation of tuple with single value

t=(233)
print(t)
print(type(t))
#here we will get the type is int bcz u r giving the paranthesis ,normally python treated as normal int
#solution give a cooma after 233

t=(233,)
print(t)
print(type(t))

#3 creation of tuple with different data items
t=(46,'priti',4.4,'True')
print(t)

#4  creation of tuple without using paranthesis
   #paranthesis are optional,but u have to give -- it is highly recomanded
t=10,'sonu',555,5.5
print(t)
print(type(t))



#5 creation of tuple using tuple function
t=[20,40,60,80]    #list to tuple
t1=tuple(t)
print(t1)  # it give tuple format output
print(t)  # list format output

#6 creation of tuple by using range
t=tuple(range(10))
print(t)

#7 creation of tuple by using string
t=tuple('priti')
print(t)
