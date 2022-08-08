# uses of * and ** in function call

print('ex-1')
def fun(a,x,y,z):
    print(a)
    print(x)
    print(y)
    print(z)
fun(10,20,30,40)

print('ex-2')
def fun(a,x,y,z):
    print(a)
    print(x)
    print(y)
    print(z)

l=[12,32,4,6]
fun(*l)
#fun(l) TypeError: fun() missing 3 required positional arguments: 'x', 'y', and 'z'
l=[2,3,4]
#fun(*l)
# there no z val thats why we are getting error
#TypeError: fun() missing 1 required positional argument: 'z'
#solution 
fun(*l,23) # now 23 store inside z
print('----')
fun(23,*l)
print(23,45,*l)



print('ex-3-------')
def fun(a,x,y,z):
    print(a)
    print(x)
    print(y)
    print(z)

l=[12,32,4]
#fun(23,45,*l)
#TypeError: fun() takes 4 positional arguments but 5 were given

# we can use list,set,tuple,dict
print('ex-4------')
def fun(a,x,y,z):
    print(a)
    print(x)
    print(y)
    print(z)

t=(12,32,4,8)
fun(*t)
print('------ set does not maintain order')
s={2,6,4,5}
fun(*s)


# how to use ** in function call
# it will store in the form of dict
print('---')
def fun(a,**s):
    print(a)
    print(type(a))
    print(s)
    print(type(s))
fun(12,k=6)

print('^^^^^^^^')
d={'p':2,'k':5}
fun(12,**d)


