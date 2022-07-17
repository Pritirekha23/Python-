#nested tuple
   # a tuple inside another tuple is known as nested tuple

t=((28,'surendra',6.4),33,(8677,6,6.4))
print(t[0])
print(t[0][1])

for i in t:
    print(t)



#inside a nested tuple  i can create a list and i can modify that list
t=((28,'surendra',6.4),33,[8677,6,6.4])
print(t[-1])
t[-1][1]='panda'  # it can be modify bcz that is a list
print(t)




#TUPLE COMPREHNSION
    # it is not possible ------ it will going to return   a generator object ,,<generator object <genexpr> at 0x000002197F009A10>
t=(i for i in range(10))
print(t)
print(type(t))

# converting generator to tuple--u can achive the value now 
t=tuple(i for i in range(10))
print(t)
print(type(t))



# advantages of tuple
   # tuple is faster than list
   # it can be used as ket for dictionary
   #it is the read only version of list


# difference b/w list and tuple
  #list is mutable where tuple is mutable
  #[] is used to created list where as() is used to create tuple
  #list cant be used as dictionary  key where as tuple can be used as a dictionary key