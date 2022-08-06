#set methods part1
   # add() ,update(),remove(),discard(),pop(),copy(), clear(),enumerate(),max(),min(),sum(),sorted()
 #these are normal methods that u can apply with any data structure .

# add() 
    # it is used to add an element into a set
    #it has no effect if the element is already present 
print('add ex-1')
s={2,5,6.6,56}
s.add('priti')
print(s)

print('add ex-2')
s={2,5,6.6,56}
s.add(56)
print(s)

#print('add ex-3')
#s={2,5,6.6,56}
#s.add(88,99)
#print(s) #TypeError: set.add() takes exactly one argument (2 given) --- so better to go for update





# update()
  # it is used to add multiple elements into a set
  #here we will going to iterable object element not individual element like list,tuple,range etc
print('update ex 1')
s={2,5,6.6,56}
l=[8,32,5,6]
t=(12,33,44,55,66)
s.update(l,t)
print(s)


print('update ex 2')
s={2,5,6.6,56}
print(s)
l=[8,32,'priti',5,6]
t=(12,33,44,'panda',55,66)
s.update(l,t,range(90,101))
print(s)



#print('update ex-3')
#s={2,5,6.6,56}
#s.update(88,99)
#print(s)  #line 50, in <module> TypeError: 'int' object is not iterable
#WHAT IS  THE DIFFERENCE BETWEEN add() and update()  ?
   # add() is used to add an element into set where update() is use to add multiple iterable(list,range,tuple etc) elemenets
   

print('update ex-4')
s={2,5,6.6,56}
s.update([88,99])
print(s)

print('update ex-5')
s={2,5,6.6,56}
s.update(range(30),range(100,126))
print(s)

# remove()
  # It is used to remove the perticular or specified element from the set .
  #if the specified element is not present then it will raise key error .
print('remove ex-1')
s={2,5,6.6,56}
s.remove(6.6)
print(s)

#print('remove ex-2')
#s={2,5,6.6,56}
#s.remove(676)  #KeyError: 676
#print(s)

# discard()
  # It is also used to remove the element from the set .
  #if the specified element is not present then it will Wont raise any error .
  # 

print('discard ex-1')
s={2,5,6.6,56}
s.discard(6.6)
print(s)


print('discard ex-2')
s={2,5,56}
s.discard(78888)
print(s)

# DIFFEREMCE BETWEEN remove() and discard()?
   # Both are used to remove the specified element from the set ,but the difference is that in discard
   # if the specified element is not present then wont raise any key error but in remove() it raise a keyerror


# pop()
  # if u want to remove and return any random element then go for pop .
print('pop ex-1')
s={2,5,200,400,56}
print(s.pop())
print(s)


#it does not take any argument
#print('pop ex-2')
#s={2,5,200,400,56}
#s.pop(5)   #TypeError: set.pop() takes no arguments (1 given)
#print(s.pop())
#print(s)

print('pop ex-3--if the set is empty then it will give an error')
#s=set()
#print(s.pop())  #KeyError: 'pop from an empty set'  



# copy()
 #it is used to return a shallow copy of a set .
 # both are pointing to different memory location  but containt are same.
 #if we will make any changes in  s1 it will not reflect to s2 and vice versa this is called as shallow copy .
print('copy ex-1')
s1={23,55,66,76,56}
s2=s1.copy()  #clonning -- same value
print(s2)
print(s1)
print(id(s1))
print(id(s2))
s1.add(3333)
print(s1)
s2.add(66666)
print(s2)


#deep copy(assigning)
 # both are pointing to same memory location  and containt are same.
 #if we will make any changes in  s1 it will reflect to s2 and vice versa this is called as shallow copy .
print('deep copy ex-1')
s1={23,55,66,76,56}
s2=s1  #assigning
print(s2)
print(s1)
print(id(s1))
print(id(s2))
s1.add(3333)
print(s1)
print(s2)



# clear()
  #it is used to remove all the lements from the set .
  #here set will not be deleted only elements are deleted
print('clear ex-1')
s={23,55,66,76,56}
print(s)
s.clear()
print(s)




# enumerate()
 # It will return an enumerate object which  contain index as well as value of all the items

print('enumerate ex-1')
s={65,74,23,90,12}
for i,j in enumerate(s):
    print(i," ",j)

# ex-2 it will give the result in the form of tuple .
print('enumerate ex-2')
s={65,74,23,90,12}
for i in enumerate(s):
    print(i)
 
print('enumerate ex-3')
s={65,74,23,90,12}
for i,j in enumerate(s):
    print(j)
    
# max()
print('max ex-1')
s={65,74,23,90,12}
print(max(s))
print(min(s))
    
# min()
print('min ex-1')
s={65,74,23,90,12}
print(min(s))


# sum()
  # it will the sum of all the elements present inside the set
print('sum ex-1')
s={65,74,23,90,12}
print(sum(s))


# sorted() 
#it will give the output as list not the form of set .
print('sorted in ascending and descending order ex-2')
s={65,74,23,90,12}
print(sorted(s))
print(sorted(s,reverse=True))




