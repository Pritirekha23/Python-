#dictionary methods
  # get()  items() pop() popitems() keys() values() setdefault() update() copy() clear() fromkeys() str()

#get()   
 # it means to get the value which is associated with the key
#by using get method then u did not get any error .
 #if the key is not present in the dict then it will give None
print('get method')
d={1:'piti',2:'riti',3:'sriti',56:'rati'}
print(d.get(56))  
print(d.get(5))  # it will give None as output
#if i dont want none if the key is not present then we can give the default value
print(d.get(5,'unknown'))
#if the key is present and i am giving the default value then we will get the value present in that key value not the default val
print(d.get(56,'unknown'))
#print(d[5])  #keyerror


# items() 
#in dict item means key and value both .
#it is used to return list of tuple that contain key and value as a pair .
print('items method ex 1')
d={1:'piti',2:'riti',3:'sriti',56:'rati'}
print(d.items())  

print('items method-ex2 print line by line')
d={1:'piti',2:'riti',3:'sriti',56:'rati'}
for i in d.items():
        print(i) 



print('items method print way 3')
d={1:'piti',2:'riti',3:'sriti',56:'rati'}
for i,j in d.items():  
  print(i,' ',j)

# pop() -
# remove and return 
#if the key is not avialable then it will raise keyerror
#it except one argument if will nort pass any argument then it will raise typeerror
print('pop method ')
d={1:'piti',2:'riti',3:'sriti',56:'rati'}
print(d)
print(d.pop(2))
print(d)
#print(d.pop()) #typeerror
#print(d)
#print(d.pop(78)) #keyerror
#print(d)



# popitems() 
   #it will going to remove the last inserted item and return that in the form of tuple
  #before 3.7 it will remove the random one from the dict
  #it does not take any argument
  #if the dict is empty then we will get keyerror that dict is empty
print('popitems method ex1')
d={1:'piti',2:'riti',3:'sriti',56:'rati'}
print(d.popitem())
print(d)
#print(d.popitem(56)) #typeerror popitem() takes no argument
#print(d)

#print('popitems method ex2')
#d={}
#print(d.popitem()) #keyerror
#print(d)






# keys() 
 #it is used to return all the keys of the dict i the foorm of list
print('keys method ex1')
d={1:'piti',2:'riti',3:'sriti',56:'rati'}
print(d.keys())

print('key method ex2')
print('printing in individual')
d={1:'piti',2:'riti',3:'sriti',56:'rati'}
for i in d.keys():
  print(i)



# values() 
#it is used to return all the values of dict on the form of list
print('value method ex1')
d={1:'piti',2:'riti',3:'sriti',56:'rati'}
print(d.values())

print('value method ex2')
print('printing in individual')
d={1:'piti',2:'riti',3:'sriti',56:'rati'}
for i in d.values():
  print(i)


# setdefault() 
#it is related to setting kind of things .
#if the key is not avialable in the dict then it will add that key and value in the dict
#if the key is  avialable in the dict then it will return that coresponding key value
#if the key is present then it will give that key value
#if the value is not present then it will add None by default
print('set default method ex1')
d={1:'piti',2:'riti',3:'sriti',56:'rati'}
print(d)
print(d.setdefault(10,'ruru'))
print(d)
print(d.setdefault(1,'ruru'))
print(d)
print(d.setdefault(56)) #it will give that key value
print(d) 
print(d.setdefault(88)) #None
print(d)

# update() 
#it is used to add all the item of one dict to another dict
  #adding or modifying
print('update method ex1')
d1={1:'piti',2:'riti',3:'sriti',56:'rati'}
print('set default method ex1')
d2={111:'rahul',66:'iam',333:'you are',506:'heyhey'}
d1.update(d2)
print('update d1')
print(d1) #update d1
print(d2)
print('update d2')
d2.update(d1)
print(d2)  #update dict
print(d1)

#if the both keys name are same then it will added the updated value  .
print('update method ex2')
d1={1:'piti',2:'riti',3:'sriti',56:'rati'}
print('set default method ex1')
d2={111:'rahul',2:'iam',333:'you are',506:'heyhey'}
d1.update(d2)
print('update d1')
print(d1) #update d1
print(d2)

# copy()
print('copy method ex1')
d1={1:'piti',2:'riti',3:'sriti',56:'rati'}
d2={}   # the container should be blank .
d2=d1.copy() #cloning
print(d2)
print(d1)
print(id(d2))
print(id(d1))
#any changes made on d1 is not reflect to d2 and vice versa bcz the id are different .
d1[1]='college'
print(d1)



print('assigning method ex')
#any changes made on d1 is  reflect to d2 and vice versa bcz the id are same .
d1={1:'piti',2:'riti',3:'sriti',56:'rati'}
d2={}
d2=d1 #assigning
print(d2)
print(d1)
print(id(d2))
print(id(d1))
d1[1]='college'
print(d1)


# clear()
#it will clear the element of the dict
d1={1:'piti',2:'riti',3:'sriti',56:'rati'}
print(d1)
d1.clear()
print(d1)



# fromkeys() 
  #if u want to creat a dict from iterable object like list,tuple then go for formkeys
print('frromkeys method example')
print('from list ex')
l=[26,87,9,35]
d=dict.fromkeys(l)
print(d)


print('from tuple ex')
l=(26,87,9,350)
d=dict.fromkeys(l)
print(d)


print('fromkeys with value e-2')
l=[20,80,90,30]
d=dict.fromkeys(l,'hello')
print(d)

print('using range')
l=(26,87,9,350)
d=dict.fromkeys(range(5),1)
print(d)
#range(5)-- iterable objct , and 1 is the value .

print('using range in the value pass list')
l=(26,87,9,350)
d=dict.fromkeys(range(5),[3,5,8])
print(d)


print('using range in the value pass tuple')
l=(26,87,9,350)
d=dict.fromkeys(range(5),(3,5,8))
print(d)

#instead of range if we will use empty list
#if there is no key then no value is there 
print('passing empty list as key')
l=(26,87,9,350)
d=dict.fromkeys([],[3,5,8])
print(d)
print('eg')
d=dict.fromkeys([],[])
print(d)

print('exampleeeee')
d=dict.fromkeys([2],[54])
print(d)

print('exampl')
d={}.fromkeys([2],[54])
print(d)

# str()



