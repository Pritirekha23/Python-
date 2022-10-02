# Is Python supports call by value or call by reference or call by object reference
# WHAT IS CALL BY VALUE
   
   # If we will made any changes on called function it will not reflect to outside.
# ex-1
print('call by value ex 1')
def fun(a):
    print('inside fun',a)
    print('inside fun',id(a))
a=24
print('outside fun',a)
fun(a)
print('outsidde function',a)
print('outside fun',id(a))

print('------')
#ex-2
print('call by value ex 2')
def fun(a):
    print('inside fun',a)
    print('inside fun',id(a))
    a=777
    print('inside the function after assigning new value to a',a)
    print(id(a))
a=24
print('outside fun',a)
fun(a)
print('outsidde function',a)
print('outside fun',id(a))

# we will going to change in object
# pass integer(imutable object)
print('call by value ex-3')
def fun(a):
    print('inside fun before modification',a)
    print('inside fun before modification',id(a))
    a=300
    print('inside fun before modification',a)
    print('inside fun before modification',id(a))

a=240
print('outside fun brfore calling',a)
print('outside fun before calling',id(a))
fun(a) # here we are passing value not address
print('outsidde function aftre calling',a)
print('outside fun after calling',id(a))
# by example 1,2,3 call by value we conculuded that python supports call by value
#only in integer(immutable)


#Call by reference  --
  # if we will made any changes in call by reference it will reflect to outside
# pass list(mutable object)
print('call by reference ex-1')
def fun(l):
    print('inside fun before modification',l)
    print(id(l))
    l.append(222)
    print('inside fun after modification',l)
    print(id(l))

l=[23,44,55]
print('outside fun before calling',l)
print(id(l))
fun(l)  # here we are passing address/reference of l instead of value
print('outsidde function after calling',l)
print(id(l))

# here if we made any changes in called function it will reflect to outside ,so this is called call by reference 




#PYTHON NEITHER SUPPORT CALL BY VALUE OR CALL BY REFERENCE 
# IT SUPPORTS ONLY CALL BY OBJECT REFERENCE
  # when you will pass any immutable object it will bhv like call by value
  # when you will pass any mutable object it will bhv like call by reference
  # so python does not support call by value and call by reference
  # it only supports call by object reference---means it depeneds upon your argument
     # means if u pass immutable object then it will bhv call by value
     # and if u pass mutable object then it will bhv like call by reference

#immutable object--- new object will create 
#mutable object--- it will not create a new object
