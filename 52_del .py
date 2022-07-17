#del (variable will remove from the memory )
#del is used for deletion purspose  and it is highly recomanded that if your variable and all the things are uses complete then use del
#1
print('del')
a=100
print(a)
del(a)
print(a) # here we get an error
#2
print('del with string')
s='priti'
print(s)
del s
print(s) #error
#we cant delete  individual character here

#3
print('list')
l=[10,20,30,40,50]
print(l)
del(l)
print(l) #error

#4
print('in the case of list we can delete individual elements')
l=[10,20,30,40,50]
print(l)
del(l[2])
print(l)  #output is [10,20,40,50]

#NOTE :
#IN THE CASE OF LIST WE CAN DELETE INDIVIDUAL ELEMENTS  BUT IN THE CASE OF STRING WE CANT DELETE INDIVIDUAL ELEMENT
