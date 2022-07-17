#transfer statement--- break,continue,pass
#A break
#how to exit from the loop ----ans---by using break
#break means exit from the loop or stop the flow of program execution
#1 print 0 1 2 3 4 5 6 7 8 but whenever the no. is 8 break the loop
print('break statement ex1')
for i in range(10):
    print(i)
    if i==7:
        break

#2
print('break statement ex2')
for i in range(10):
    if i==7:
       break
    print(i)


#B continue(skip) -- it will go back to the loop
# continue means if u want skip some itteration or part then go for continue
#1
print('continue statement ex1')
for i in range(10):
    if i==5 or i==8:
        continue
    print(i)

#2  here 50 is not present bcz the range is 11 so it will print 1 to 10
print('continue statement ex2')
for i in range(11):
    if i==50:
        continue
    print(i)

#C pass keyword means empty statement
# it is workful in empty statement
#if u want to provide empty body then go for pass statement
#do nothing means pass
#1 print only even numbers 
print('only even numbers between 10 using pass keyword')
for i in range(10):
    if i%2==0:
       print(i)
    else:
        pass

#2 print only odd numbers 
print('only odd numbers between 10 using pass keyword')
for i in range(10):
    if i%2==0:
       pass
    else:
        print(i)