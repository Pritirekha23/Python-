#Wap to find out the number of occurrences of a character present in a string .

s='mamami ji 3244544'
d={}
for i in s:
    #for creating items and updation .
    d[i]=d.get(i,0)+1   
print(d)
for i,j in d.items():
    print(f'{i} is present {j} times')