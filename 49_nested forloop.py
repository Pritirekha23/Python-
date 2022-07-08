#nested(inner) for loop
# If a for loop is present inside another for loop is known as nested for loop
#1
for i in range(3):
    for j in range(3):
        print('i={} j={}'.format(i,j))

 #2   
for i in range(3):
    for j in range(3):
        print('*')

#3
for i in range(3):
    for j in range(3):
        print('*',end='') #after this line we want a space
    print('')

#4
for i in range(3):
    for j in range(3):
        print(i) 
    
#5
for i in range(3):
    for j in range(3):
        print(i,end='') #after this line we want a space
    print('')

#6
for i in range(3):
    for j in range(3):
        print(j,end='') #after this line we want a space
    print('')

