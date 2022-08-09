#dictionary comperhension
print('dict comprehnsions ex1')
d={k:k for k in range(1,6)}
print(d)
print(type(d))

print('dict comprehnsions squaring formex2')
d={k:k*k for k in range(1,6)}
print(d)
print(type(d))

#find the area of  circle
print('working with list to create dict comprehensions ex')
l=[2,3,4.2,5.6,7.8]
d={i:3.14*i*i for i in l}
print(d)

#length of name
name=['surendra','priyanka','kim namzoon','jungkook']
d={i:len(i) for i in name}
print(d)

#display the length of name if the length is gretaer than 6
name=['surendra','priyanka','kim namzoon','jungkook','zini','rahul']
d={i:len(i) for i in name if len(i)>6}
print(d)