#WAP TO SEARCH AN VALUE FROM A LIST THEN DISPLAY ITS INDEX ,
# IF THE VALUE  PRESENT MULTIPLE TIMES THEN PRINT ITS ALL INDICES AND
#  ALSO COUNT THE NO. OF TIMES THAT VALUE IS REPEATED IN THE LIST



l=[10,12,14,16,14,18,20,14,30,14]
i=0
count=0
key=int(input('enter the key to serach from the list'))
while i<len(l):
    if key==l[i]:
        print(f'{key} is present at {i} index')
        count+=1
    i=i+1
print(f'{key} is present  {count} times')