#nested dictionary 
   # if a dictionary is present another dictionary then it is called as nested or inner dictionary .

#example
print('example 1 of nested dictionary ')
d={1:{'name':'smruti'},2:{'name':'msmi'},3:{'name':'jyoti'},4:{'name':'priti'}}
#print(d)

#only values
for i in d.values():
    print(i)

#only key
for i in d:
    print(i)

#key with value
for i,j in d.items():
    print(i,' ',j)

print(d[1])
print(d[1]['name'])


print('example 2 of nested dictionary')
d={1:{'name':'smruti'},2:{'name':'msmi'},5:{6:{7:{8:9}}}}
print(d[5])
print(d[5][6])
print(d[5][6][7])
print(d[5][6][7][8])
d[5][6][7][8]=198989898
print(d[5][6][7][8])
print(d)
