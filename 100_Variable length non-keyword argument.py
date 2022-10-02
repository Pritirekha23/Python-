#Variable length argument 
  # what the requirement of Variable length argument ? 
    # To  pass n number of argument .
  #it is two type Variable length argument 

    #1> variable length non-keyword argument(*args)
    #2> Variable length keyword argument(**args)

#1> variable length non-keyword argument(*args)
 #ISSUES--
def fun(A,b,c,d,e):
  print(A,b,c,d,e)
#fun(10,20,30,40,50,60)  #-->here we cant pass 60 bcz the size is 5
fun(10,20,30,40,50)


#solution
 # *means any numebr of argument
 # (*a)it is storing the data in the form of tuple data structure.
print('example-1 of variable length non-keyword argument')
def fun(*a):
  print(type(a))
  print(a)
fun(12,3,44,55,66,676)
fun(4,54,32,2,1,13,6,7,8,899,9)
fun(12)
fun()


print('example-2 of variable length non-keyword argument')

def fun(*args):
  print(args)
fun(12,3,4,3.2,[2,4,6,7],True,False,20+3j)

print('example-3 of -variable length non-keyword argument +positional argument')
def fun(x,*a):
  print('x is ',x)
  print('a is ',a)
fun(20,30)
fun(19,30,40,50)

#def fun(*a,x):
 # print('x is ',x)
  #print('a is ',a)
#fun(20,30)

# fun() missing 1 required keyword-only argument: 'x'
# here *a means it can hold n number of arguments so when we pass fun(20,30) all two values are stored inside a and nothing is for x thats why its showing an error


#SOLUTION
#fun() missing 1 required keyword-only argument: 'x'
print('solution')
def fun(*a,x):
   print('a is ',a)
   print('x is ',x)
 
fun(20,30,67,x=23)
#u cant write like this fun(x=23,20,30,67) bcz positional argument follows keyword ,if u write then u will get an error

print('example---a')
#def fun(x,*a):
 #  print('a is ',a)
  # print('x is ',x)
 
#fun(20,30,67,x=23)
#TypeError: fun() got multiple values for argument 'x'
print('example-b')
#After passing variable length argument u can pass keyword argument otherwise it will going to treat all the thing as a single entity.

def fun(*a,x):
   print('a is ',a)
   print('x is ',x)
 
fun(x=23)

#default argument+ variable length non-keyword argument
print("exaple--111")
def fun(*A,x=12):
  print('A is',A)
  print('x is',x)
fun(88)
fun(223,445,778,976,86,2.2) # default value of x is taking here
fun(3,4,5,6,7,x=30)
#here the value of x is 30
#fun(x=3,4,5,6,7,30) # SyntaxError: positional argument follows keyword argument


print("exaple--112")
def fun(x=12,*A):
  print('A is',A)
  print('x is',x)

fun(125,342,56)
#fun(88,34,54,6,7,x=38) #TypeError: fun() got multiple values for argument 'x'


#keyword argument + positional argument + variable length argument
print("exaple--113 ,k+p+d")
def fun(a,b,*n,x=10):
  print(a)
  print(b)
  print(n)
  print(x)

fun(122,333)



print("exaple--114 ,k+p+d")
def fun(a,b,*n,x=10):
  print(a)
  print(b)
  print(n)
  print(x)

fun(21,345,67,89,554,33,x=666)


print("exaple--115 ,k+p+d")
def fun(a,b,x=10,*n):
  print(a)
  print(b)
  print(n)
  print(x)

#fun(21,345,67,89,554,33,x=666)
#TypeError: fun() got multiple values for argument 'x'
fun(12,4,6,7788,989,5)


print("exaple--116 ,k+p+d")
#def fun(x=12,a,b,*n):
  # non default argument follows default argument
  #print(a)
  #print(b)
  #print(n)
  #print(x)

#fun(2,4,5,56)



print("exaple--117,k+p+d")
def fun(a,b,x=10,*n):
  print(a)
  print(b)
  print(n)
  print(x)

#fun(12,34,x=23,22,33)
#positional argument can not appear after keyword argument





















