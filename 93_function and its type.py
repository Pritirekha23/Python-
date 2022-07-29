# function and its types 
 
 #function :-
   # It is just like small part of our program,used to perform specific task
   # function means sub program or mini program
   # It is nothing but collection of function statement that are kept inside a block
   # It is also called as subroutine or procedure in other language .
# Advantages :-
  #code reusability
  # improve modularity/readability

# if we will not use function it means same code we will copy and paste multiple times .

# It is two types --
  # Build in function(predefined/primitive/primary/libarary functions) -- ready-to-use
  # User defined function

# define user define function 
  # def keyword is used to defined user defined function
  # when we call the function it will execute ,so function is not execute automatically.

print('ex 1 addition of 3 number')
def add(a,b,c):
    '''This function is used to perform addition of 3 numbers'''
    print(a+b+c)
add(10,20,30)
add(9.9,6,4)
print(add.__doc__)   # description of functions

# doc string means information about  particular functions .



# difference between parameter vs  argument -
# parameter --  it is just like variable that present in function definition
#parameters means input to the function
#  add(a,b,c) -- a,b,c are called parameter

#argument -- An argument is value that is send to the function at the time of calling
#  add(9.9,6,4)--9.9,6,4 are called argument

print('ex-2')
def num(a,b,c):
    print('inside function')
    print(id(a))
    print(id(b))
    print(id(c))
    print(a,b,c)
a,b,c=10,20,30
num(a,b,c)
print('outside function')
print(a,b,c)
print(id(a))
print(id(b))
print(id(c))

# outside fun of a,b,c  id is same as parameter a,b,c id -- pointing to same memory location
 # here parameter and argument are pointing same memory location

print('ex-3')

def num(x,y,z):
    # if the value is not same then it will point into different memory location
    print('inside function')
    print(id(x))
    print(id(y))
    print(id(z))
    print(x,y,z)
a,b,c=10,20,30
num(a,b,c)
print('outside function')
print(a,b,c)
print(id(a))
print(id(b))
print(id(c))


print('ex-4')
# now x memory location will change bcz we modify the x value
def num(x,y,z):
    print(id(x))  # here the memory location of x is same to a bcz holding same value 
    x=999   # here we modify x so the memory location of x is change here
    print('inside function')
    print(id(x))
    print(id(y))
    print(id(z))
    print(x,y,z)
a,b,c=10,20,30
num(a,b,c)
print('outside function')
print(a,b,c)
print(id(a))
print(id(b))
print(id(c))