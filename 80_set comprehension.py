#Set comprehension
   # WHAT IS THE REQUIREMENT OF set comprehension ?
      # If u want to create a set from the iterable objects like tuple,list,set,dict,range etc . by writing less
      # code in efficient way then we can go for set comprehensions .

#benift  of
  # less code (techincally called coinside code)
  # very fast set comprehension

# create a set from list

print('creating set from list without set comprehension')
l=[23,564,77,87,33]
s=set()
for i in l:
   s.add(i)
print(s)

print('creating set from list with set comprehension')
l=[23,564,77,87,33]
s={i for i in l}
print(s)


print('creating set from list ex-1')
l=[23,564,77,87,33]
s={i*2 for i in l}
print(s)


print('creating list from list ex-2')
l=[23,564,77,87,33]
s={i**2 for i in l}
print(s)



print('creating set from list ex-3')
l=[23,564,77,87,33]
s={i-5 for i in l}
print(s)

# WORK WITH range

print('working with range ex -1')

s={i for i in range(100,111)}
print(s)


print('working with range ex-2')

s={i**2 for i in range(11)}
print(s)



# create a set by adding all the element from 20 to 40 which is divisible by 4
print('example')
s={i for i in range(20,41) if i%4==0}
print(s)


#create a set from list called as name by adding the 1st chracter of each element
print('working with string ex 1')
name=['priti','smruti','kriti']
s={i[0] for i in name}
print(s)

print('working with string ex2 make the 1st character to upper')
name=['priti','smruti','kriti']
s={i[0].upper() for i in name}
print(s)

#create a set from a list(name) by adding all the elements but if the element is priti then
#instead of priyanka add daaa
name=['priti','smruti','kriti']
s={i if i!='priti' else 'doo' for i in name}
print(s)