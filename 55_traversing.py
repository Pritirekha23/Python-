#Traversing in list
#visiting all the element in a sequence is called traversing
#1) Traversing list using loop
print('traversing list using for loop')
l=[10,12,14,16,18]
for i in l:
    print(i)
#here 1st time i will point to index 0 element(10) then 1 ,2 like this

#2)l=[10,12,14,16,18]
#start=0,stop=4,step=1
l=[10,12,14,16,18]
print('traversing list using while loop ex1')
i=0
while i<=4:
    print(l[i])
    i=i+1
#3)l=[10,12,14,16,18]
#start=0,stop=4,step=2
l=[10,12,14,16,18]
print('traversing list using while loop ex2')
i=0
while i<=4:
    print(l[i])
    i=i+2

#if i dont know the size of the list ,then find out the length of the list and then put
#4) l=[10,12,14,16,18]
#start=0
l=[10,12,14,16,18]
print('traversing list using while loop ex3 finding the length')
i=0
while i<len(l):
    print(l[i])
    i=i+1
#5)l=[10,20,36,64,72,91,811,34,544,888]
# if the value is divisible by 4 and 8 then only u can display
l=[10,20,36,64,72,91,811,34,544,888]
for i in l:
    if i%4==0 and i%8==0:
        print(i)