#range data type ---used to represent a sequence of no.
#1
r=range(10)
for i in r:
    print(i)
 #2
print("------")
r1=range(1,20)
for j in r1:
    print(j)
#3
print("------")
r2=range(1,20)
for j in r2:
    print(j)
#4
print("******")
r4=range(5,15,2)
for k in r4:
   print(k)
#5
print("&&&&%&&&&")
pr=range(10)
print(pr[2])
print(pr[6])
#The no. in the range are not modifiable or immutable
print("#####")
r3=range(10)
print(r[0])
print(r[3])
r3[5]=39 
print(r3[5])   