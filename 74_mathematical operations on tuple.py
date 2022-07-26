#BASIC MATHEMATICAL OPERATIONS ON TUPLE


#1  Concatenation operation (+)
print('  Concatenation operation on tuple')
t1=(323,4,5,6)
t2=(44,66,77,88)
t3=('priti','sonu','4.4')
t=t1+t2+t3
print(t)
t=t2+t1+t3
print(t)

#2  Repetition operation on tuple(*)
print('  Repetition operation on tuple')
t=(323,4,5,6)
tt=t*4
print(tt)


#3 Traversing operations 
print('traverse using for loop')
t=(323,4,5,6)
for i in t:
    print(i)


print('travesre using while loop')
t=(323,4,5,6)
i=0
while i<len(t):
    print(t[i])
    i=i+1

