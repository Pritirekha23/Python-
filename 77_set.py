#set
  #if u want to store only unique data then set is required .
  # u cant apply indexing and slicing concept .
  #list and tuple data structure allows dupliacte elements .
  #set does not maintained orderd .
  #set is unorderd collection .
  # we can store heterogeneous data item .
  # set is mutable in nature based on your requirement we can modification operations .
  # {} curly brackets is used to create set data structure .
  # NOTE:-
    # set--mutable , setelemnts-immutable   
      # We can modify set but we cant modify its content ,hence set is mutable but its elements are immutable in natureb .



# creation of set in different wat

#1  creation of empty set
#s={}
#print(s)
#print(type(s))
#this is a dictionary       

# we can create empty set by using set function
s=set()
print(s)
print(type(s))



#creation of set with  multiple  elements
#set does not maintain order
s={22,44,56,77}
print(s)
print(type(s))




#creation of set with  heterogeneous  elements
s={22,44,56,77,'priti',2.2,'False'}
print(s)
print(type(s))

#creation of set using set() function
    #creation of set from list
l=[33,44,55,66]
s=set(l)
print(s)
print(type(s))

  #creation of set from tuple
l=(33,44,55,66)
s=set(l)
print(s)
print(type(s))


  #creation of set from range()
s=set(range(10))
print(s)
print(type(s))

  #creation of set from string
name='pritirekha panda'
s=set(name)
print(s)
print(type(s))



#
name='pritirekha panda'
s=set(name.split())
print(s)
print(type(s))

#

s=set('pritirekha panda')
print(s)
print(type(s))


#WE CANT APLLY INDEXING AND SLICING CONCEPT
#error
#s=[3,4,5,6,7,78]
#print(s[2])
#print(s[::])  


# in and not in
s={33,55,76,'priti','til',8.6,3}
print('priti' in s)
print('til' not in s)
print('prit' in s)
print('til' in s)