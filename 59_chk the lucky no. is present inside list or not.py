#WAP TO CHECK WHETHER YOUR LUCKY NUMBER IS PRESENT INSIDE THE LIST OR NOT
#by using in operator

l=[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
choice=int(input('enter your lucky number::'))

if choice in l:
    print('yes..your lucky number is present inside the list')

else:
    print('no...your lucky number is not  present inside the list')