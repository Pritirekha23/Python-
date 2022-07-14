#WAP to print list in reverse order
#way 1-- suing +ve index

print('way 1 using +ve index')
l=[10,20,30,40,50]
#start=4,step=-1,stop=0
r=len(l)-1

while r>=0:
    print(l[r])
    r=r-1



print('way 2 using -ve index')
l=[10,20,30,40,50]
#start=-1,step=-1,stop=-5
i=-1

while i>=-len(l):
    print(l[i])
    i=i-1