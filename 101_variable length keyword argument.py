# variable length keyword argument(**kwargs)
#Requirement
 # To pass key and value as a pair at the particular time we can use variable length keyword argument
# This function does not take any argument.
#This data will store in the form of dictionary
print('vlk ex-1')
def fun(**a):
    print(type(a))
    print(a)
#fun(12,33)
#TypeError: fun() takes 0 positional arguments but 2 were given
fun(x=10,y=29)
fun(x=3,y=5,z=[12,3,4],z1={1:2,2:4,5:'priti'})



print('ex-2')
def fun(x,**a):
    print(a)
    print(x)
#fun(a=3,b=7,c=34)
#TypeError: fun() missing 1 required positional argument: 'x'
fun(x=34,a=6,b=3)

print('ex-3')
def fun(x,**a):
    print(a)
    print(x)
fun(a=2,b=3,c=4,d=5,x=55)
fun(55,a=2,b=3,c=4,)


print('ex-4')
def fun(x,*k,**a):
    print(a)
    print(x)
    print(k)

fun(55,a=2,b=3,c=4,)
fun(322,4,5,33,3,333,a=8,b=7)


print('ex-5')
#def fun(x,**a,*k):
   # we cant write variable lentgh keyword argument aftyer variable length non-keywordarguement.
#    print(a)
 #   print(x)
  #  print(k)
#fun(2,a=2,b=4)
#SyntaxError: invalid syntax

print('ex-6')
def fun(**a):
    print(a)
fun()
fun(a={})
#fun(x=99,y=44,222,33,33)
#SyntaxError: positional argument follows keyword argument

print('ex-7')
def fun(*b,**a):
    print(b)
    print(type(b))
    print(a)
    print(type(a))
fun()
fun(x=8,y=2)



