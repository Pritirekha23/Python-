# string method part 2
#splitting of string 
#split()  ----  for the separation purpose it is used .... it will used to return a list ,once it found spcae means it treated as one element
print('split method ex1')
s='pritirekha panda'
print(s.split())

print('split method ex1')
s='pritirekha panda'
print(s.split('a'))


print('split method ex3')
s='pritirekha panda'
print(s.split('p'))

print('split method ex4')
dob='1-1-2000'
print(dob.split('-'))


print('split method ex5')
dob='1-1-2000'
print(dob.split('*'))   # star is not present so it give that dob as a single element

#join()
print('join method ex 1')
l=['priti','rahul','raja']
s='+'.join(l)
print(s)

print('join method ex 2')
l=['priti','rahul','raja']
s='*'.join(l)
print(s)

print('join method ex 3')
l=['priti','smruti','jyoti']
s=''.join(l)
print(s)

print('join method ex 1')
l=('33','44','55')
s='+'.join(l)
print(s)


#Remove the space from the string
#istrip()
#rstring --- right side 
print('istrip method ex1')
s='surendra           '
print(len(s))
print(len(s.rstrip()))

#lstrip-- left side
print('istrip method ex2')
s='               surendra'
print(len(s))
print(len(s.lstrip()))



#strip-- both side
print('istrip method ex2')
s='               surendra       '
print(len(s))
print(len(s.strip()))


#fill character 

#zfill()
print('zfill example 1')
s='surendra'    #10-8=2
print(s.zfill(10))


print('zfill example 2')
s='surendra'    
print(s.zfill(5))  #nothing happen bcz size is 5

print('zfill example 3')
s='surendraaa'    #50-10=40
print(s.zfill(50))



#rjust()  --- 1st time it will add the string in right side
print('rjust ex 2')
s='hello'
print(s.rjust(10))    #10-5= 5-- it add 5 space from left side

print('rjust ex2')
s='surendra'
print(s.rjust(10))   #10-8=2---from left side it add 2 space


print('rjust ex3')
s='surendra'
print(s.rjust(10,'*')) 


print('rjust ex4')
s='surendra'
print(s.rjust(40,'*')) 


#ljust() ---1st it will print the string in left side then it will add 
print('ljust ex1')  
s='surendra'
print(s.ljust(10,'*')) 

#center()
print('center ex 1')
s='sonu'
print(s.center(20))

print('center ex 2')
s='sonu'
print(s.center(20,'*'))

print('center ex 3')
s='sonu'
print(s.center(23,'*'))



#other
#min()
s='ansuman'
print(min(s))
print(max(s))
print(sorted(s))   #return in the form in list ascending order
print(sorted(s,reverse=True))   #descending order


#isidentifire()
#it check whether your string is a identifire or not
  #identifire name can not start with digit
s='233prit'
print(s.isidentifier())
s='abc233'
print(s.isidentifier())
s='True'
print(s.isidentifier())
s='***uhh'
print(s.isidentifier())

#enumerate()
s='priti'
for i,j in enumerate(s):
    print(i,j)

