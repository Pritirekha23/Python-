#DICTIONARY DATA STRUCTURE PYTHON
     #why we learn dictionary ds?
        #in the case of list,set,tuple  we can store only value .
        # but in dictionary we will store key and value as a pair thats why we will use dictionary .

#WHAT IS DICTIONARY ?
   #ANS-  It is a inbuild data structure in python , it is used to store key and value as a pair .
       #we will use curly bracket to create dictionary
#ex--    'name':'pritirekha panda'  here name is key and pritirekha panda is the dictionary .
#example :--


print('dictionary example 1')
myinfo={
    'name':'pritirekha panda',
    'github':'Pritirekha23',
    'email':'pandapriti@gmail.com',
    'address':'Bhadrak'
}
print(myinfo['name'])
print(myinfo['github'])
#print entire dictionary
print(myinfo)


#CHARACTERSTICS OF DICTIONARY
  # Dictionary is mutable(changable) in nature so that we can perform modification based on our requirement .
  # Duplicate keys(just like id orunique) are not allowed ,but duplicate values are allowed .
  # dictionary is dynamic(growable) in nature means based on our requirement we can increase and decrease the size .
  # we cant aplly indexing and slicing concept in dictionary .
  # Heterogeneous elemnts are allowed .
  # Dictionary keys are case sensitive .

print('dictionary example 2')
myinfo={
    'name':'pritirekha panda',
    'Name':'Pritirekha23',
    'email':'pandapriti@gmail.com',
    'address':'Bhadrak'
}
print(myinfo)


#Duplicate keys(just like id orunique) are not allowed,it will update that value
print('dictionary example 3')
myinfo={
    'name':'pritirekha panda',
    'name':'Pritirekha23',  #it update the value
    'email':'pandapriti@gmail.com',
    'address':'Bhadrak'
}
print(myinfo)



#DIFFERENT WAYS FOR CREATING DICTIONARY
# creating empty dictionary
print('ways of creating dict ex-1')
d={}
print(d)
print(type(d))

#create empty dict then add item .
print('ways of creating dict ex-2')
d={}
print(d)
d['name']='RM'
d['address']='korea'
d['email']='bts@gmail.com'
print(d)
print(type(d))

#create dict directly
print('ways of creating dict ex-3')
roll={1:'priti',2:'Ani',3:'sruti'}
print(roll)
print(roll[1])
#print(roll[11])  --#key error bcz 11 key is not present
print(type(roll))

#creation of empty dictionary using dict()
print('ways of creating dict ex-4')
d=dict()
print(d)
print(type(roll))


#How to check whether a specified elememt is present(exist) or not
 #By using has_key()   
#print(' dict ex-5')
#roll={1:'priti',2:'Ani',3:'sruti'}
#print(roll.has_key(2))   # it will produce an error bcz has_key() is present in the python 2ndversion .

# solution--
  #use in operator 
print('ex-6')
roll={1:'priti',2:'Ani',3:'sruti'}
print(2 in roll)
print(2 not in roll)
print(5 in roll)
print(d)

# Traversing a dict
print('traversing of dict ex 1')
roll={1:'priti',2:'Ani',3:'sruti'}
for i in roll:
    print(i)   # i will point to key here 


# how to print key and val
print('traversing of dict ex 2')
roll={1:'priti',2:'Ani',3:'sruti'}
for i in roll:
    print(i,roll[i])


# CREATE A DICTIONARY DYNAMICALY BY TAKING USER INPUT .
print('CREATE A DICTIONARY DYNAMICALY BY TAKING USER INPUT ')
d={}
while True:
    key=input('enter the key::')
    val=input('enter the val::')
    d[key]=val
    choice=input('do u want to add more element[y/n]::').lower()
    if choice=='n':
        break


# add , modify ,delte dictionary item 
  # add item :-
print('add item in dict ex 1')
roll={1:'priti',2:'Ani',3:'sruti'}
print(roll)
roll[78]='priya'
print(roll)

   #modify item:-
print('modify item in dict ex 1')
roll={1:'priti',2:'Ani',3:'sruti'}
print(roll)
roll[1]='priya'
print(roll)
#if the key is not available then it will add the key and val in the dict
roll[122]='yoyu'
print(roll)



   #delte item:-
print('delete item in dict ex 1')
roll={1:'priti',2:'Ani',3:'sruti'}
print(roll)
del roll[1]
print(roll)
#if the key is not available then it will produce an error in the dict
#roll[122]='yoyu'
#print(roll)
print('delete all the elements of dict')
roll.clear()
print(roll)

#how to delete entire dictionary
#del roll
#print(roll)  # NameError: name 'roll' is not defined  ,bcz the dict is deleted 




#DID U KNOW 
   # i)dict key are always immutable in nature that means we cant use  it list,set,dict as a dict key
   # ii)hence we cant use list,set,dict as dictionary key why because they all are mutable
   # in nature ,but we can use numbers,tuple,frozenset ,string as dict key otherwise we will get type error

#i using list as key dict
#print('example u cant use list as a key in dict----1')
#d={[1,2,3]:'priti',2:'Ani',3:'sruti'}
#print(d)

#ii using set as key dict 
#print('example u cant use set as a key in dict----1')
#s=set()
#d={s:'priti',2:'Ani',3:'sruti'}
#print(d)


#iii using tuple as a key dict
print('iii')
print('example u can use tuple as a key in dict----1')
d={(1,2,3):'priti',2:'Ani',3:'sruti'}
print(d)


#iv using frozenset as key dict
print('iv')
fs=set((10,20,30))
d={frozenset(fs):'pritiiii',2:'rama',3:'raju'}
print(d)
print(d[frozenset({10,20,30})])
print(d[frozenset(fs)])


#v using dict as key and val
#d={{1:'tu'}:'priti',2:'Ani',3:'sruti'}
#print(d)  #Type error

#usingdict as a val
print('we can use dict as the value but we cant use as a key')
d={1:{1:'tu'},2:'Ani',3:'sruti'}
print(d)


# vi   use float
print('vi')
roll={2.5:'priti',2:3.4,3:'sruti'}
print(roll)


#vii  use complex 
print('use complex vii')
roll={10+6j:'priti','tuu':12+98j,3:'sruti'}
print(roll)


#viii use boolean
print('use boolean')
roll={True:'priti',2:True,3:'sruti'}
print(roll)











