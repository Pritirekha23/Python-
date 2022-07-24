# WHAT IS THE NEED OF FUNCTION ?
   # ans---   if we want to execute or run the same piece of code multiple times then we can go for function .
   # it will improve the readability of code 
   # it will also improve the modularity ,means can divide a large program into multiple small part .

#check a number is even or odd .
print('program without using function example 1')
#here the readabilty decreases bcz we are writing the same code evry time .
a=14
if a%2==0:
    print('even ')
else:
    print('odd')
b=20
if a%2==0:
    print('even ')
else:
    print('odd')
b=25
if a%2==0:
    print('even ')
else:
    print('odd')



print('program using functions ex-1')
#here we are using minimum code as comare to the previous program .
def evenodd(num):
    if num%2==0:
        print('even')
    else:
        print('odd')
evenodd(100)
evenodd(14)
evenodd(20)
evenodd(25)