#CONCATENATE OF LIST
#  jointing oflist is known as Concatation of list.
# + operator  is used to concatenate list.
# we can concatenate multiple list
# u can only concatenate list .
#ex-1
print('CONCATENATE OF LIST ex1')
l1=[23,56,98,65]
l2=['priti','56',88,'arti']
l3=[44,4.4,88,99]
r=l1+l2+l3
print(r)

#ex-2
print('CONCATENATE OF LIST ex2')
l1=[23,56,98,65]
l2=['priti','56',88,'arti']
l3=[44,4.4,88,99]
r=l1+l3+l3
print(r)

#ex-3
print('CONCATENATE OF LIST ex3')
l1=[23,56,98,65]
l2=['priti','56',88,'arti']
l3=[44,4.4,88,99]
r=l1+l3+l2
#based on the sequence it will add .
print(r)


# here + operator only work with list if both arguments list then it will concatenate,if arguments are diffrent then it will raise error
#ex-4
#print('CONCATENATE OF LIST ex4 rasing error bcz of different arguments')
#l1=[23,56,98,65]
#l2=100
#r=l1+l2
#print(r)






#REPETITION OF LISTS
  # REPETITION  means it will repeat based on specified number of times 
  # * opeartor is used to repear the list.
  #here we cant give the float value . it accept only integer .
  #we cant multiply l*l
  #example 1
print('repetiton ex 1')
l=[10,20,30,40,50]
r=l*5
print(r)

#we cant multiply l*l(error produce)
  #example 2
#print('repetiton ex 2')
#l=[10,20,30,40,50]
#r=l*l
#print(r)

#we cant give the float value 
  #example 3
#print('repetiton ex 3')
#l=[10,20,30,40,50]
#r=l*3.2
#print(r)



#MEMBERSHIP IN LISTS---
 # it is  used to check whether the specified element is the member of the particular list or not.
 #there are 2 operator we will use to check membership .
 # (i) in operator (ii) not in operator

 #example 1
print('membership  in list')
l=[65,64,99,66]
print(64 in l)
print(64 not in l)

print(644 in l)
print(644 not in l)

