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


#(c)--->
