#list comprehnsion
# WHAT IS THE REQUIREMENT OF list comprehnsion?
   # ANS--- If u want to create a list from iterable objects like list,tuple,range,dict etc. by writting very less code in efficient way then we can go for list comorehsions.
 #advantages:
     # we will creat iterable objects--list,tuple,dict etc
     #performance wise it is very good(taking less time)
     #less code
    #example
from ast import comprehension


print('ex-1')
l=[i for i in range(11)]
print(l)

print('ex-2')
l=[i*i for i in range(11)]
print(l)

print('ex-3')
l=[i**i for i in range(11)]
print(l)

print('ex-4')
l=[i+2 for i in range(11)]
print(l)



print('with list comphrension ex-5')
l=[i for i in range(1,21) if i%2==0]
print(l)

print('without using list comprehension')
l=[]
for i in range(1,21):
    if i%2==0:
        l.append(i)
print(l)
#ex6
# name=['surendra','priyanka','zini']
#expected output : ['s','p','r','z']
print('ex-6')
name=['surendra','priyanka','zini']
l=[i[0] for i in name]
print(l)

# it is also applicable for slicing concept
print('ex-7')
name=['surendra','priyanka','zini']
l=[i[0:4] for i in name]
print(l)

#create a new list  by add the element which is contaning letter a
print('create a new list  by add the element which is contaning letter a')
name=['surendra','priyanka','zini']
l=[i for i in name if 'a' in i]
print(l)


# creat a list ,if the name is priyanka instead of priyanka add hello
print("")
name=['surendra','priyanka','zini']
l=[i if i!='priyanka' else 'hello' for i in name]
print(l)


#create a list from tuple
print('ex-t1')
t=(10,20,30,99)
l=[i for i in t]
print(l)

print('ex-t2')
t=(10,20,30,99)
l=[i for i in t  if i%6==0]
print(l)

#create a list from string
print('working with string')
name='prit'
l=[i for i in name]
print(l)

#creation of matrix using list comprehnsion .
print('matrix using list comprehnson ex 1')
m=[[j for j in range(3)] for i in range(3)]
print(m)


print('matrix using list comprehnson ex2')
m=[[j for j in range(5)] for i in range(5)]
print(m)


print('matrix using list comprehnson ex3')
m=[[i for j in range(3)] for i in range(3)]
print(m)


print('matrix using list comprehnson ex4')
m=[[i*j for j in range(3)] for i in range(3)]
print(m)

