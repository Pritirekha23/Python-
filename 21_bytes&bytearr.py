#bytes --we cant modifie the values here 
a=[10,12,14,16,18] #list range is 0 to 255 (included)
b=bytes(a) #list to bytes  here b is holding a all values
print(b[2])
print(b[-2])
print(b[0])

#modify 1st index value (cant possible modification)
b[1]=23
#if u want to print all the elements then we have to use  loop
for i in b:
    print(i)
print(b[5]) #error that 5 index is not present
b1=[122,257,34,33] #here we get an error bcz the range is 0 to 255
c=bytes(b1)
print(c[1])
print(c[-2])
