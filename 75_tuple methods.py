#tuple methods
 # actually tuple is having two methods --- 1) index 
 # 2)count  
 # 3) cmp() -> now  it is outdated it is available in python 3

# list all  methods are used to modify the list ,so those functions are not available in tuple


# we can use other normal method along with tuple
  # 4) len()
  # 5) min()
  # 6) max()
  # 7) sorted()

#1 index() --- it will return index of first occurance of the given element

print('index method')
t=(22,66,76,87,98,76,76)
print(t.index(76))


#1 count() --- it will return the specified element present  how many number of times
t=(22,66,76,87,98,76,76)
print(t.count(76))

#3 cmp() function -- is used to  compare tuples but in pyhton 3 version onwards it is outdated .
# it is outdated .
 
#print('cmp function')
#t1=(10,11)
#t2=(10,1)
#t3=(10,1)
#print(cmp(t1,t2)) #1
#print(cmp(t2,t1)) #-1
#print(cmp(t2,t3)) #0

#HOW IT WORKS
 # if first tuple is greater than the second tuple then it will return 1 else -1
 # if both tuple are same then it will return 0

#NOTE:--
    # instead of cmp() function we will simply use == != >< symbol for comparision


#4 len()-- it is used to calculate the length of tuple
print('length')
t=(22,66,76,87,98,76,76)
print(len(t))


#5 min() and  #6 max()--- used to calculate the min and max value of tuple
print('min and max')
t=(22,66,76,87,98,76,76)
print(min(t))
print(max(t))

#7 sorted() --> by default it will sort in ascending order.
    # it will return the result in list format not in tuple .
print('sorted a tuple in ascending ')
t=(222,6,3,8,98,7,76)
t1=sorted(t)
print(t1)

# sorted() in descending order by passing reverse=True
print('sorted a tuple in descending ')
t=(222,6,3,8,98,7,76)
t1=sorted(t,reverse=True)
print(t1)


#8  tuple packing and  unpacking
# packing--individual to group
print('packing')
a=8
b=9
c=4
d='surendra'
e='2.2'
t=a,b,c,d,e     #packing
print(t)
print(type(d))
print(type(t))

#NOTE:-
# At the time of unpacking the number of variables and number of value must be same
#unpacking -- group to individual
t=(2,4,5,'prit',5.5)
a,b,c,d,e=t
print(a,b,c,d,e)
print(type(t))
print(type(d))

#by using tuple we can return multiple value from function
# in python a function can return multiple value
def fun():
    l=[32,4,5,67,7]
    return(l[0],l[2],l[3])
t=fun()
print(t)








