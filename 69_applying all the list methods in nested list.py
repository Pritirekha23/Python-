
# we can apply all the method of list here

#reverse this list:--
print('reverse of the list')
l=[10,20,30,[40,50,60],70,80,90] 
l.reverse()
print(l)

#append() 
print('add end  of the list')
l=[10,20,30,[40,50,60],70,80,90] 
l.append(222)
print(l)


#remove()
print('remove  of the list')
l=[10,20,30,[40,50,60],70,80,90] 
l.remove(30)
print(l)




#index() 
print('index of the list')
l=[10,20,30,[40,50,60],70,80,90] 
print(l.index(70))




#count() 
print('count the list')
l=[10,20,30,[40,50,60],70,30,80,90] 
print(l.count(30))




#pop()
print('pop of the list')
l=[10,20,30,[40,50,60],70,80,90] 
l.pop()    # it will remove the last one
print(l)   

l.pop(3)
print(l)



#extend() in nested list
print('extend() of the list')
l=[10,20,30,[40,50,60],70,80,90]
l1=[44,444,55,77,[99,11,29],65,90]

l.extend(l1)
print(l)

#clear()
print('clear of the list')
l=[10,20,30,[40,50,60],70,80,90] 
l.clear()   
print(l) 




#copy() 
print('copy() of the list')
l=[10,20,30,[40,50,60],70,80,90]
l1=l.copy()
print(l)
print(l1)


#insert() 
print('insert() of the list')
l=[10,20,30,[40,50,60],70,80,90]
l.insert(3,444)
print(l)

# we cant sort list with individual element(int)
#sort()
print('sort of the list')
l=[10,20,30,[40,50,60],70,80,90]
print('before sort')
print(l)
print('after sort')
l.sort()
print(l)

