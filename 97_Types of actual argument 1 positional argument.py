# Types of Actual Argument :--
   # what is requirement of actual argument
      #ans-- The actual arguments is used in a function call
   #1)Positional argumnet
   #2)Keyword argument
   #3)Default argument
   #4)Variable length argument

#1)Positional argumnet
   # Positional argument means at the time of functional calling we will pass these  arguments in CORRECT POSITIONAL ORDER , otherwise  we may get unexpected result. This is also called required argument.
   

print('positional argument ex-1')
def cal(a,b,c):
    print(a+b*c) 
     #2+2*3   --> * has more priority so 2*3=6 , then + , 6+2=8
cal(2,2,3)
cal(3,2,2)

#cal([3,2,6],[4,5,6],[2,3,4])    
# print(a+b*c) TypeError: can't multiply sequence by non-int of type 'list'
# The number of positional argument and parameter (define in function header ) must be same.


print('positional argument ex-2')
def cal(a,b,c):
    print(a,b,c) 
     
cal(2,2,3)

#cal(2,2) # type error, cal() missing 1 required positional argument: 'c'

#cal([2,4,5]) # this is a list it will store only in a so here we get an TypeError: cal() missing 2 required positional arguments: 'b' and 'c'

# cal() TypeError: cal() missing 2 required positional arguments: 'a' 'b' and 'c'  

cal([3,2,6],[4,5,6],[2,3,4])
cal((),[],{})


print('positional argument ex-3')
def fun():
    print('hello python!')

fun()
#fun(4) #TypeError: fun() takes 0 positional arguments but 1 was given
#fun(None)
#None means it will treat as one argument ,TypeError: fun() takes 0 positional arguments but 1 was given
#fun(0)
#TypeError: fun() takes 0 positional arguments but 1 was given

def sum(x,y):
   c=x+y
   print(c)
x=2;y=3
sum(x,y)