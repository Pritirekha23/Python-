#what is Nested list---
   # If a list is present inside another list then it is called as Nested list.
   # ex ---->>> l=[10,20,30,[40,50,60],70,80,90] 

#1
print('nested list example 1')
l=[10,20,30,[40,50,60],70,80,90] 
print(l[2])
print(l[3])
print(l[-4])
print(l[3][1])
print(l[3][-1])
print(l[-4][-1])

#2

print('nested list example 2')
l=[10,20,30,[40,50,60],70,80,90,['priti','smruti','tiki'],3.7,6.5]
print(l) 
print(l[7])
print(l[3])
print(l[-3])
print(l[4])
print(l[2:6])   # 6 is  not included .
print(l[::])



#3
print('nested list example 3')
l=[10,20,30,[40,50,['rutu','kunu'],60],70,80,90,3.7,6.5]
print(l[2])
print(l[3])
print(l[3][2])
print(l[3][2][1])
print(l[-6][-2])



# NESTED LIST AS A MATRIX
 
# this l is contain 3 element 
print("Without loop print row")
l=[[10,20,30],[40,50,60],[39,49,50]]
print(l)
#printing in row wise
print(l[0])
#print(l[0][2])  =30
print(l[1])
print(l[2])


#print row wise using loop
#if we have 100 row is there then we have to use loop
print("With loop print row")
l=[[10,20,30],[40,50,60],[39,49,50]]
for i in l:
    print(i)

print('printing in one line')
l=[[10,20,30],[40,50,60],[39,49,50]]
for i in l:
    print(i,end='')




print(' ')   #...not required ok
#if u dont want to print the bracket and the comma then ..
print('without bracket and comma')
l=[[10,20,30],
[40,50,60],
[39,49,50]
]
for i in l:
    for j in i:
        print(j,end='  ')
            #end with space means control will not jump to next line
    print(' ')

