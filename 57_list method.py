#list methods
# append(),insert(),count(),index(),remove(),pop(),extends(),reverse(),sort(),clear(),copy()
#
#(a)---->append() method---joint at the end(it is used to add element  at the end of the list),loaction is not required bcz it add the element at the end
#it will work like push() opearation of STACK data structure
#1
print('This is the append method')
l=[23,64,87,98,45]
print('before adding element at the end the list containing elements are')
print(l)
l.append(800)
l.append(454)
print('after adding element at the end the list is')
print(l)

#2  WAP TO CREATE A LIST BY ADDING 20 0's
print(' LIST BY ADDING 20 0s')
l=[]
for i in range(20):
    l.append(0)
print(l)
#3  WAP TO CREATE A LIST BY ADDING 0 to 20
print(' LIST BY ADDING 0 to 20 0s')
l=[]
for i in range(21):
    l.append(i)
print(l)

#(b)--->insert() method-- it is used to insert itemat specific location(index),here location is required
# drawback of append()--it will add element at the end only---but as a programmer sometimes we have a requirement to add the element as a specific position 
#so we cant solve this by using append(),so insert() came into the picture
#1)ex-1
print('This is insert method')
l=[32,43,65,76,87]
print('befor adding 666 in location 3')
print(l)
l.insert(3,666)
print('after adding 666 in location 3')
print(l)
l.insert(4,888)
print(l)

#NOTE--1
#if the specified positive index crossed the maximum index ,then it will be inserted at the end of the list.
#here it will behave like append()---adding the element at the last
#2 ) ex-2
print('This is insert method ex-2')
l=[32,43,65,76,87]
print('befor adding 999 in location 30')
print(l)
l.insert(30,999)
print('after adding 999 in location 30')
print(l)
print(l.index(999))
#it will give the index of 999 is 5 bcz 30 is crossed the maximum index ,so it will add the element at the last or end of the list

#NOTE--2
#if the specified -ve index crossed the minimum index ,so it will be inserted at the beginning of the list.
print('this is insert method ex-3')
l=[76,76,36,98,88]
print(l)
l.insert(-40,555)
print(l)
print(l.index(555))
#it will give the index of 555 is 0 bcz -40 is crossed the minimum index ,so it will add the element at the beginning of the list

#WHAT IS THE DIFFERENCE BETWEEN APPEND() AND  INSERT():--
 #ANS---append() method it is used to add element  at the end of the list . insert() method-- it is used to insert item at specific location.
 #in insert() method ,if the specified positive index crossed the maximum index ,then it will be inserted at the end of the list.
 #here it will behave like append()---adding the element at the last,if the specified -ve index crossed the minimum index ,so it will be inserted at the beginning of the list .


#(c)--->count() method-- it is used to the number of times an element appears in the list
#NOTE:-
   #If the element is not appears in the list then it will return 0.

#1
print('Example of count method')
l=[88,66,44,99,44,44,88,44,66,888]
print(l.count(44))  
 #if here i write only l.count(44) --then it will give blank screen ,bcz it is giving  3 as output so we have to print that output
print(l.count(999))
print(l.count(88))


#(d)--->index() method --->it is used return the specified element index.
#if the number is repeated in the list then it will give the 1st present number index value 
  # index method ex-1 ---in this example 44 is present 4 times at index 2,4,5,and 7 , here it always return the lowest index means  here 44 's lowest index in this example i.e 2 (lowest index value of 44)
#if the value is not given in the list then we will get an value error
print('index method ex-1')
l=[88,66,44,99,44,44,88,44,66,888]
print(l.index(44)) 
#print(l.index(73466)) 
# here we will get a value error bcz here the value 73466 is not present



#(e)  remove() method------>it is used to remove the specified element from the list.
        # if the specified element present multiple times, then it will remove the first occurance from the list.
     # if the value is not present in the list it will give an value error
#ex-1
print('remove method')
l=[10,12,14,12,16,18,20,12,55,12]
print('before removing')
print(l)
l.remove(12)
print('after removing 12')
print(l)
print('after removinh 18')
l.remove(18)
print(l)
#l.remove(444)     # here we will get an value error bcz 444 is not present in the list 
#print(l)
#print(l.remove(12))   #here it will give blank as output ,bcz here does not return anything ,so why we print this...

#(f)   pop()---> by default  it is used to remove and return the last element of the list
# it will work on two way  one is default bhv  and another is based on our requirement 
# if u want to remove any specified element then we have to provide that specified element index .
print('pop method ex-1')
l=[32,44,55,66,77,777]
#print(l.pop())  #if u print like this then it will give that value which one is deleted or u want delete
l.pop()
# it will renmove the lastone i.e here 777
print(l)
#print(l.pop(1))
l.pop(1)
print(l)

#l.pop(89)
#print(l)
#here we get an index error bcz 89 index is not present in the list




#WHAT IS DIFFERENCE BETWEEN REMOVE AND POP METHOD?
#ANS-- remove()--- here u have to provide the value .it is used to remove the specified element from the list.
        # if the specified element present multiple times, then it will remove the first occurance from the list and if the value is not present in the list it will give an value error
#pop()-- here u have to provide the index .by default  it is used to remove and return the last element of the list
# it will work on two way  one is default bhv  and another is based on our requirement 
# if u want to remove any specified element then we have to provide that specified element index .


#(g) extends() method -->
     #it is used to add the element of one list into another list .
     # example --1
print('ex-1 of expands method')
oldGFlist=['C','JAVA','PYTHON','PHP','MYSQL']
newGFlist=['AI','ML','IOT','Blockchain','AR/VR']
oldGFlist.extend(newGFlist)
print(oldGFlist) 
#example --2
print('ex-2 of expands method')
l1=['C',2,2.2,34]
l2=['hello',6,2.8,0]
l1.extend(l2)  
#here i am adding the l2 value in l1 so we have to print l1 
print(l1) 
#example --3
print('ex-3 of expands method')
l1=['Python',2,2.2,34]
l2=[5,6,2.8,0]
l2.extend(l1)
print(l2) 
#print(l1) #here it will give only the l1 value bcz in this example we are adding th element of l1 into l2,so we have to print the l2 value(where we add print that value)




#(h) reverse() method-->
   #it is used to  reverse a list
#example -1
print('reverse method ')
l=[65,76,22,660,777]
l.reverse()
print(l)




#(i) sort() method-->
  #it is used to arranging elements either in ascending or in descending order.
#example -1
print('sort method ex-1 print in ascending order')
l=[67,44,22,33,99]
l.sort() 
print(l) 
#example -2
print('sort method ex-2 print in descending order')
l=[67,44,22,33,99]
l.sort(reverse=True) 
print(l) 
#if u write (reverse=True) ,then it will print the element in descending order

#NOTE-
    #(i)if list is contain numbers then it will work based on ascending and descending order.
    #(ii)--but if the list contain string then it will work in alphabet order (just like english dictionary)
    #(iii) if the list contain heterogeneous elements then in this case sort() will not work  , but it will work on python 2nd version...1st it will print the numbers after that it will prit string data.
#example of ii
print('sorting of string example of (ii)')
l=['smruti','jyoti','swati','priti']
l.sort()
print(l)
#example of iii--
#print('sorting od string example of (iii)')
#l=['smruti','jyoti','swati','priti',88,77,443]  
#l.sort()
#print(l)
#type error is occured here



#(j)  clear() method-->
  # it is used to clear or remove all the elements of list . clear means not delete.
#here list are present and eleemnts are delted from the list so it will give  a empty list
#example-1
print('clear method example 1')
l=[1,2,3,4,5,6]
print(l)
l.clear()
print(l)
#example-2
#print('clear method example 2')
#l=[1,2,3,4,5,6]
#print(l)
#del l    
 #here entire list is deleted so we get an error
#print(l)




#(k) copy() method-->
  # It is used for shallow copy ,here shallow copy means if we made any modification in the new list wont be reflected in the originsl list .
  #Both list will pointing to different memory location .
   #copy--different ,assign--same
#example-1
print('copy method ex-1')
l1=[23,44,66,77,88]
l2=l1.copy()   #cloning
print(l1)
print(l2)
#it will give diffrenet memory loaction
print(id(l1))
print(id(l2))

l2[3]=6666
print(l1)
print(l2)

#ASSIGNING (equals to )
#example of assigning
#if we made any modification in the new list will  be reflected in the originsl list .
  #Both list will pointing to same memory location 
print('assigning method ex-')
l1=[23,44,66,77,88]
l2=l1  #assigning
print(l1)
print(l2)
#it will give same memory loaction
print(id(l1))
print(id(l2))

l2[3]=6666
print(l1)
print(l2)

#differenece between copy and assign 
  #ans-->>copy--different ,assign--same