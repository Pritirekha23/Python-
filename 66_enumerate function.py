#enumerate() function
#requirement---if u want to print index  as well as value at a time .
#in normal way more code is required but using enumerate() less code is required .
print('This is the example 1 of enumerate function way 1')
l=[65,74,23,90,12]
for i in enumerate(l):
    print(i)

#good way
print('This is the example 1 of enumerate function way 2')
l=[65,74,23,90,12]
for i,j in enumerate(l):
    print(i," ",j)

