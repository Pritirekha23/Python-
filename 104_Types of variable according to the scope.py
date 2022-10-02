#Types of variables according to the scope
# We can not access all the variables at all locations of the programs it always depend on the variables where we declared.
# two types---local variable and global variable

# Local variable
  # The variable which is declared inside the function , is called local variable.
  # we can access local variable only with in that function.


print('local variables ex-1')
def fun1():
    a=25 #local variable
    print(a)
# u can access this a inside fun1() only
#def fun2():
 #  print(a)
fun1()
#fun2() #NameError: name 'a' is not defined 

#Global variables:-
 # The varibales which is declared outside the function is called Global variable.
 #These variables we can access through out the program.

print('Global variable example-1')
a=25
def fun():
  print(a)

def fun1():
  print(a)
fun()
fun1()
print(a)