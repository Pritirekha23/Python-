#for loop 
#for loop along with range function 
#1display your name 10 times by using for loop
 
for i in range(10):
    print('Pritirekha panda')

#2 print 1 2 3 4 5 6 7 8 9 10
#start=1 stop=10(here i write 11(forward so 11) means 11 is not included)step=1 
for i in range(1,11,1):
    print(i)

#3) 2 3 4 5 6 7 8
#start=2 step=1 stop=8(8 included so if i write 9 means 9 is not included so it print  upto 8)
 #(start,stop,increment/decrement)
for i in range(2,9,1):
    print(i)

#4)200 400 600 800 1000
#start=200 stop=1000 step=200
for i in range(200,1001,200):
    print(i)

#5)print 10 9 8 7 6 5 4 3 2 1 
#start=10 stop=1(1 not included so we 0(backward so 0)) step=-1
for i in range(10,0,-1):
    print(i)

#6)print 999 777 555 333 111
#start=999 stop=111(111 not included means 110(bcz it is backward) )
for i in range(999,110,-222):
    print(i)

#7)print all the even number from 100 to 120
for i in range(100,121,1):
    if i%2==0:
        print(i)
    
    #solving this problem without using for loop
for i in range(100,121,2):
    print(i)


#8) working with string::::---i is ittereting with number of items
# #it will print individual character in new line(vertical)
name='pritirekha panda'
for i in name:
    print(i)

#9
name='rama hari sita'
for i in name:
    print(i,end="-")

#10
name='rama hari sita'
for i in name:
    print(i,end="")
