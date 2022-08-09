# DIFFERENCE BETWEEN PRINT AND RETURN STATEMENT

# print vs return

# print--
  # print is used to print data in console
  # used for printing purpose only means just for displaying to end user
  # we cant use this printing for further purpose
  # we can write print() any no. of times anywhere of our program
#return--
  # It is used to return one or multiple value to called function
  # return means not printing or displaying , if we will return something means it will not show to the end user .
  # we can use value for further uses .
  # if we will write return statement means it will exit from that function .
def fun(a):
    print(a*a)
    print(a+a)
    print(a+a)
    return a+3
    print(a/a)  # not execute 
fun(5)
  # we cant write return statement any where .
  # return must be your last statement of that function .

# print and return both are completely different things in python .


# it will execute one time so here we can write like this .
def fun(b):
    if b>6:
      return b
    else:
        return b-2
print(fun(4))
