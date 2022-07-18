#Frozenset 
#it is the advance version of set .
  # Forzenset is similar to set data structure but there is only difference is that forzenset is 
  # immutable in nature ,so that we can perform modification operations .
  ### frozen set is immutable in nature so we cant use add(),remove(),kind of methods why bcz these will modify frozenset
#creation of frozenset() from set
print('frozen set ex-1')
s={67,4,5,6,8}
fs=frozenset(s)
print(fs)
print(type(fs))

#creation of frozenset() from list
print('frozen set  from list ex-2')
s=[6,77,4,5,6,8]
fs=frozenset(s)
print(fs)
print(type(fs))

#creation of frozenset() from range
print('frozen set from rang ex-3')
fs=frozenset(range(5))
print(fs)
print(type(fs))


#print("###")
#fs=frozenset(range(10))
#fs.add(88)  #atribute error
#fs.remove(76)    #atribute error

# we camn apply normal function which will not modify the frozen fumction
# APPLYING OTHER FUMCTION

print('ex-1')
fs1=frozenset([23,76,98,77,54])
fs2=frozenset([78,744,22,77,666])
fs3=frozenset([798,65])
fs5=frozenset([98,56])
fs4=fs1.copy()
print(fs4)

print(fs1.union(fs2))
print(fs1.intersection(fs2))
print(fs1.difference(fs2))
print(fs1.symmetric_difference(fs2))
print(fs1.issubset(fs2))
print(fs1.issuperset(fs2))
print(fs1.isdisjoint(fs2))
print(fs3.isdisjoint(fs5))