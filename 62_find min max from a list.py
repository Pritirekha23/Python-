#WAP TO FIND MIN AND MAX VALUE FROM THE LIST



print('min value in the list')
l=[32,44,55,66,2,77,99]
min=l[0]
#start=1,stop=6
for i in l:
    if i<min:
        min=i
print('min is::',min)

print('max value in the list')
l=[32,44,55,66,2,77,99]
max=l[0]
#start=1,stop=6
for i in l:
    if i>max:
        max=i
print('max is::',max)
