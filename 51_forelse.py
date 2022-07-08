#for else
# for loop along with else block
#if for loop executed successfully without having break then only else block will execute

#1
print('for else without break')
for i in range(10):
    print(i)
else:
    print('i am else block if the else block executed succssfully then only i will execute')

#2  if break executed inside for loop then else block wont be execute
print('for else with break')
for i in range(10):
    if i==5:
        break
    print(i)
else:
    print('i am else block if the else block executed succssfully then only i will execute')
