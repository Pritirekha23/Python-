#input
# l=['Smruti','Priti','Jyoti','Swati']
#output
# 
print('way 1')
l=['Smruti','Priti','Jyoti','Swati']
new_List=[]

for i in l:
    new_List.append(i[0]+i[-1])
print(new_List)


print('way 2')
l=['Smruti','Priti','Jyoti','Swati']
new_List=[]

for i in l:
    r=len(i)
    new_List.append(i[0]+i[r-1])
print(new_List)