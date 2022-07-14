#wap to display the elemets of a list along with possitive and negative index
#suppose we have a lis l=[23,33,43,53,64]
#expected ouput---
#23 is present at index 0/-5
#33 is present at index 1/-4
# 43 is present at index 2/-3
# 53 is present at index 3/-2
# 64 is present at index 4/-1
#1
print('only the value only')
l=[23,33,43,53,64]
for i in l:
    print(i)
#2
print('print value with +ve index only')
l=[23,33,43,53,64]
n=len(l)
for i in range(n):
    print(l[i],i)
    #n=n value is 5 ----0,1,2,3,4,5----
#3  this is the correct way of solving this problem
print('print value with -ve index')
#n=5-----0-5=-5,0-4=-4,0-3=-3,0-2=-2,0-1=-1
l=[23,33,43,53,64]
n=len(l)
for i in range(n):
    print('{} is present at index {}/{}'.format(l[i],i,i-n))