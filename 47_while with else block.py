#while with else block
#if while block executed successfully then only else block will be execute
#1
print('without break')
i=1
while i<=10:
    print(i)
    i=i+1
else:
    print('This is else block')
#2 if while block is break in the middle then it would not be execute
print('with break')
i=1
while i<=10:
    if i==4:
        break
    print(i)
    i=i+1
else:
    print('This is else block')