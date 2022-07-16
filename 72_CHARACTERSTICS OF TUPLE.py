#CHARACTERSTICS OF TUPLE
   # Tuple is immutable(unchangable) in nature .
   #Tuple can hold different data item .
   #Tuple maintaining order .
   # Duplicate elements are allowed .
   # () paranthesis is optional but it is recomanded .
   # tuple support both positive and negative index .


#1    Tuple is immutable(unchangable) in nature .
#TypeError: 'tuple' object does not support item assignment
t=(10,20,30,40)
#t[1]=99  #we cant change the value 
print(t)

#2 Tuple maintaining order .
t=(10,20,30,40)
print(t[1])

#3  Tuple can hold different data item 
t=(45,6.6,'priti','False')
print(t)

#4 Duplicate elements are allowed .
  # identify the duplicate based on index
t=(87,34,66,87,34)
print(t)

#5 () paranthesis is optional but it is recomanded .
t=10,'sonu',555,5.5
print(t)

#6 tuple support both positive and negative index .
t=(10,20,30,40)
print(t[-1])
print(t[3])