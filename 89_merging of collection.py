# merging of collections

#list merging
print('list merging')
l=[29,30,48,58]
s=[455,699,'priti']
j=l+s
print(j)

print('list merging using *')
l=[29,30,48,58]
s=[455,699,'priti']
j=(*l,*s)
print(j)
#tuple merging
print('tuple merging')
l=(29,30,48,58)
s=(455,699,'priti')
j=l+s
print(j)

print('tuple merging using *')
l=(29,30,48,58)
s=(455,699,'priti')
j=(*l,*s)
print(j)
#set merging
#set merging is not possible by using concatenation operator so here we get type error
#print('set merging')
#l={29,30,48,58}
#s={455,699,'priti'}
#j=l+s
#print(j)

# * maens all the element ,we can apply this in all the collection except dict ,in dict we will use **
print('set merging')
l={29,30,48,58}
s={455,699,'priti'}
j={*l,*s}
print(j)


# dict merging
# here if u will write  only one * then it will give only the key 
d1={1:'smruti',2:'msmi',3:'jytoi'}
d2={4:'priti',5:'raja'}
d3={*d1,*d2}
print(d3)


#solution
# here if u will write double start ** then we will gate key and value
d1={1:'smruti',2:'msmi',3:'jytoi'}
d2={4:'priti',5:'raja'}
d3={**d1,**d2}
print(d3)
