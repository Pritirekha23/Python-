#bytearray  --it is same as bytes but the difference us here we can modifie the elements
a=[10,11,12,13,14,15]
b=bytearray(a) #convert list to bytearray
print(b[1])
print(b[-2])
print("------")
#modify 1st index value
b[1]=23
for j in b:
    print(j)
    
