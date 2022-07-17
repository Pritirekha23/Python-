#LIST-------
#collection--->>>(single variable can hold multiple data)we will going to create a single variable and store multiple datas that is collection
#list data structure

   # What is the requirement of list and how list came into the picture?
    #ans --- By using fundamental data type like int,float,complex,bool and str
    # we can store one value at a time but if u want to store multiple value at a time into as a single
    #entity then we may use list (not only list we can use other collection also),
    #to over come this problem list into the picture

#INTRODUCTION TO LIST-----
   #List is an inbuild data structure in python, which is used to store
   #heterogeneous(different)data item means dissimilar data item.
    #also u can store homogeneous data
    # list is acting as a container where we can store comma separated value in between square brackets.
    #L=[23,55,'priti',True,2.2] ----L is variable name  ,and items are present in the square bracket
#NOTE1:
   #Here python list is just like array in other PL,but here the difference is that
   # it can store heteregeneous(dissimilar/different)data items
   # but in array it can hold only homogeneous(similar)data items
   #  
#NOTE2:
  #list can hold any complex datatype like dict,tuple etc  
#Example1
print('list example1')
l=[23,00,76,'priti','smruti','jyoti',2.2]
print(l)
print(l[3])
#example2
print('list example2')
l=[23,00,76,'priti','smruti','jyoti',2.2]
print(l[-4])
print(l[3])



##CREATION OF LIST IN VARIOUS WAY/METHODS----

#method-1 creation of empty list::--
   # l=[]  # the lsit is empty so it does not give any thing
   #print(l)  #it will print this-[]
print('creation of empty list')
l=[]
print(l)

#method-2 creation of list dynamically by using eval()fun^n
  # l=eval((input('enter a list::')))
  #print(l)
  #ex1
  #if u want to convert list by usng eval()then write eval()
print('printing a list by using eval() function')
l=eval((input('enter a list::'))) #at the time of entering the list u have to follow the rules(store comma separated value in between square brackets.)
print(l)

#method-3 creation of list using list()fun^n
  #l=list((12.2,'elina',12))
  #print(l)
     #ex1
print('creation of  list using list()')
l=list((12.2,'elina',12))
print(l)

     #ex2 --creation of list by using range function
      #21 is not included so it will print 10 to 20
print('creation of list by using range function')
l=list(range(10,21))
print(l)
       #ex3  --by default it will start from 0 and move towards 20(0 to 20 output)
l=list(range(21))
print(l)

#method-4
#creation of list directly
#1
print('creation of list directly')
l=[22,44,'pritiiiii',True,8.8]
print(l)
#2
#dictionary is a complex data type,ex-{'name':'Kimnamjoon'}--name=this is key and Kimnamjoon-this is value,,list((10.20,76)---this is tupple
print('ex2')
l=[23,{'name':'Kimnamjoon'},list((10.20,76))]
print(l)

#method-5
#creation of list by using split()function::
#whenever we will get a space i want to spli it
#ex-1
print('split')
msg='hello this is python'
l=msg.split()
print(l)
#ex-2
#if there is nothing then it will split based on  space but if we provide a character then based on that character it will split
print('split')
msg='hel-lo-th-is-is py-thon'
l=msg.split('-')
print(l)



#CHARACTERSTICS OF LIST
  #(based on your requirement)list is maintaining order,means in which order we inserted elements in same order it will stored in list
  #here duplicates are also allowed
  #list holds(heterogeneous) different types of data items
  #list is dynamic(growable--based on your requirement u can increase or decrease the size) in nature
  #list is mutable(changable/modify) in nature ,means based on our requirement we can modify or change the list items.
  #we can access list elements by using  index(both +ve and -ve ) and slice operator
  #list contain complex level objects like module,dict,tuple,class etc

#ACCESSING OF LIST ELEMENTS::
#there are two way ---1=index 2= slice operator
  #Accessing element by using index
print('Accessing element by using index')
l=[10,20,'rama',44,3.2]
print(l[3])
print(l[-3])
#print(l[66])# here we will get an index error bcz 66 index is not present in the list
  #Accessing element by using opearator
print('Accessing element by using slice opearator')
l=[10,20,30.9,'tara',77]
print(l[::])
print(l[1::2])