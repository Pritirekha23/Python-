#List comparision by using Equality and Relational operator .
#Equality operator 
# 1 (==)
print('example 1  equality operator')
l=['surendra','priyanka','rahul','zini']
s=['Surendra','Priyanka','Rahul','zini']
p=['surendra','priyanka','rahul','zini']
print(l==s)  
#false here l and s --case are not same
print(l==p)
#true bcz all cases are same here
#it will return true?
  #if number of elements are same .
  #content are same
  #order are same and
  #Case are also same
#2  
print('example 2 equality operator')
l=[10,38,49]
p=[38,49,10]
print(l==p)
#false here the content are same but the order are not same
print(l!=p)
#true


#Relational operator
#it will return  True?
  #here only first element will compare thats it.
#1
print('example 1 of relational operator')

l=['Surendra','Priyanka','Rahul','zini']
s=['surendra','priyanka','rahul','zini']
p=['surendra','priyanka','rahul','zini']
print(l>s)  
# S>s(this is false bcz we know that according to ASCII code s is greater than S)
#2
print('example 2 of relational operator')
a=[10,20,30]
c=[9]
print(a>c)