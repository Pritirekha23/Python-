#wap to calculate the sum of numbers from m to n 
# m=7 n=11

m=int(input("enter m value"))
n=int(input("enter n value"))
sum=0
while m<=n:
    sum=sum+m
    m=m+1
print(sum)