# Introduction to return statement
#if u not use any return statement by default python give None
  #  statement each and every function internally return a value called as None .
 #None- nothing 




print('ex-1')
def fun(p):
    print(p)
print(fun(10))  #None



print('ex-2')
def fun(p):
    print(p)
    return p*p
print(fun(10))  #100


print('ex-3')
def fun(p,s):
    print(p,s)
    return p+p
print(fun(10,20)) 


print('ex-4')
def fun():
    l=[56,87,50]
    return l
x=fun()
print(x)
for i in x:
    print(i) 

print('ex-5')
def fun():
    t=(56,87,50)
    return t
x=fun()
print(x)
for i in x:
    print(i) 

# it will always return a value to called function
#A function may or may not return a value(default it will return None))
# we cant write return statement outside function . if u write then error will produce .
# Return statement we have to write at the end of the function
# If we write any statement after return statement then it will not execute those statements.

print("examples--a")
def fun():
    print('hiii')
    return 10
print(fun())
#return 10 --- error (cant write return in outside)


print("example ---b")
def fun():
    print('good night')
    print('good morning')
    return 20
    #after return if u write any statement it will not execute
    print('good afternoon')
    print('good good ')

fun()


print('example--c')
def fun():
    print('good night')
    print('good morning')
    print('good afternoon')
    print('good good ')
    return 20
fun()

# In other PL function can return only one value 
#python can return multiple value at a time
print('example-d')
def fun(a,b,c):
    return a,b,c
print(fun(18,30,50))


print('example- e')
def fun(a,b,c):
    return a+2,b*2,c-1
t=fun(18,36,50)
print(t)


print('example-we cant write like this e')
def fun(a,b,c):
    return a+2,
   # return b*2,
   # return c-1
t=fun(18,36,50)
print(t)

print('example- f')
def fun(a,b,c):
    return a,b,c
x,y,z=fun(18,36,50)
print(x,y,z)


# benifit of return multiple value
  #111--DEFINE A FUNCTION IT WILL TAKE SIX SUBJECTS MARK OF A STUDENT AS AN ARGUMENT THEN RETURN TOTAL MARK AND AVERAGE MARK

print('111')
def cal(p,c,m,b,i,e):
    tm=p+c+m+b+i+e
    print('Total mark is',tm)
    avgmark=tm/6
    return avgmark


print('average mark is',cal(60,60,80,70,98,56))

print('------')
# or here we will gate output in the form of tuple
def cal(p,c,m,b,i,e):
    tm=p+c+m+b+i+e
    print('Total mark is',tm)
    avgmark=tm/6
    return tm,avgmark


print(cal(60,60,80,70,98,56))
tm,avgmark=(cal(60,60,80,70,98,56))
print('total mark is ',tm)
print('average mark is',avgmark)