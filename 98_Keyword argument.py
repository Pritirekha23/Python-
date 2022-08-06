# 2) Keyword argument
  # ISSUES WITH POSITINAL ARGUMENT 
     # At the time of functional calling we will pass these  arguments in CORRECT POSITIONAL ORDER , otherwise it we may get unexpected result


# by using keyword argument we cal solve this issues.
 #Keyword argument
     # In Keyword argument at the time of function calling we have to pass these arguments by using keyword(parameter name).Here order is not important

print('positional argument example')
def cal(a,b,c):
    print(a+b*c)
cal(b=3,a=2,c=4)
#Here order is not important.
#cal(a=2,c=3) #TypeError: cal() missing 1 required positional argument: 'b'

#IMPORTANT FOR INTERVIEW --- 
# Positional argument and Keyword argument
#
# Yes u can use both at a time,
print('keword argument and positional argument example')
def cal(a,b,c):
    print(a+b*c)

cal(a=2,b=4,c=5)
cal(2,b=3,c=4)
#cal(5,2,b=3)
# TypeError: cal() got multiple values for argument 'b'
#cal(2,a=4,b=5) 
# in a we give two value so here c is misising so here we get an type error   cal(5,2,b=3)
#  cal(2,a=4,b=5) TypeError: cal() got multiple values for argument 'a'

#cal(5,b=6,8) 
#SyntaxError: positional argument follows keyword argument
#After keyword argument we are passing positional argument thats why here we get an error
# NOTE--we cant provide positional argument after keyword argument
#cal(a=2,4,5)    cal(a=2,4,5) SyntaxError: positional argument follows keyword argument

#cal(3,a=3,5)
#SyntaxError: positional argument follows keyword argument --- 1st it will check the syntax thats why here we get synatx error instead of multiole value error



def cal(a,b,c,d,e,f):
    print(a+b*c)
cal(8,2,3,3,7,2)
#cal(8,2,3,e=3,7,2)
#SyntaxError: positional argument follows keyword argument
#cal(8,2,3,3,5,e=7)
#TypeError: cal() got multiple values for argument 'e'
cal(7,32,4,9,5,f=2)

def cal(a,b,d,f,c,e):
    print(a+b*c)
cal(8,2,3,3,c=5,e=7)  

#PREMIMUN POINT
    # first we have to take positional argument then keyword argument 
    # SyntaxError: positional argument follows keyword argument