#input
#l1=['Hi','Hlo']
#l2=['smruti','priti','jyoti','swati']

#output-
#['Hismruti', 'Hipriti', 'Hijyoti', 'Hiswati', 'Hlosmruti', 'Hlopriti', 'Hlojyoti', 'Hloswati']
print('problem 1')
l1=['Hi','Hlo']
l2=['smruti','priti','jyoti','swati']
new_List=[]

for i in l1:
    for j in l2:
        new_List.append(i+j)
print(new_List)




#input
#l1=['Hi','Hlo']
#l2=['smruti','priti','jyoti','swati']

#output-
#['Hi  smruti', 'Hi  priti', 'Hi  jyoti', 'Hi  swati', 'Hlo  smruti', 'Hlo  priti', 'Hlo  jyoti', 'Hlo  swati']
print('problem  2')
l1=['Hi','Hlo']
l2=['smruti','priti','jyoti','swati']
new_List=[]

for i in l1:
    for j in l2:
        new_List.append(i+'  '+j)
print(new_List)