# Types of python Recursion
# Direct recursion
# Indirect recursion
# Tail recursion
# Non-tail recursion(Head recursion)

# Direct recursion 
 #if a function call same function again , it is as direct recursion.
print('example of direct recursion--1')
def fun(n):
    if n==6:
      return
    else:
     print(n)
     fun(n+1)
fun(1)

# Indirect recursion
 # not-direct
  # if we have two functions fun1 and fun2,inside fun1 body we will call fun2 and inside fun2 body we will fun1 is called indirect recursion.
  # These  two functions are indirectly recursive bcz they call each other.


print('example of indirect recursion--1')

def fun1(n):
    if n<=5:
        print(f' fun1 = {n*2}')
        fun2(n+1)
    return

def fun2(n):
    if n<=5:
        print(f'fun2 = {n*100}')
        fun1(n+1)
    return
fun1(1)


























