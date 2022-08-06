#set methods part 2
  # set methods (used for mathematical operations)
  #methods are ---
    # union() , intersertion() , difference() , symmetric_difference() , issubset() , issuperset()  isdisjoint()
    
# union()
    # it is used to return all the element present in both set.
    #The common element we will get only once .
print('union method')
A={12,44,55,664}
B={15,12,664,88}
print(A.union(B))
print(A|B)

# intersertion() 
 #It will used to return all the common elements present in both set
print('intersertion method')
A={12,4,2,2,8}
B={2,12,15,6}
print(A.intersection(B))
print(A&B)


# difference()
 # it is used to return all the elements  present in set A not in B and vice versa
print('diffrerence method')
A={12,44,55,664}
B={15,12,664,88}
print(A.difference(B))
print(A-B)
print(B.difference(A))
print(B-A)
# symmetric_difference() 
 #It used to return all the element present in set A or B but not in both
 # excluding the common element it will return all other element
print(' symmetric_difference method')
A={12,44,55,664}
B={15,12,664,88}
print(A. symmetric_difference(B))
print(A^B)



# issubset() 
  #If  all the elements of B is present inside A then B is subset of A
print(' issubset method')
A={12,44,55,88,15,444,664}
B={15,12,664,88}
print(B. issubset(A))   #True
print(A.issubset(B))   #False

# issuperset() 
  # If  all the elements of B is present inside A then A is superset of B .
print(' issuperset method')
A={12,44,55,88,15,444,664}
B={15,12,664,88}
print(B. issuperset(A))   #False
print(A.issuperset(B))   #True

# isdisjoint()
  # there is no relationship between A and B
  #there is no common element ,both are different
print('disjoint method')
A={12,44,55,88,15,444,664}
B={3,2,4,9}
print(A.isdisjoint(B))
print(B.isdisjoint(A))