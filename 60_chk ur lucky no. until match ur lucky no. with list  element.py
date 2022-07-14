#WAP TO CHECK YOUR LUCKY NUMBER UNTIL MATCH YOUR LUCKY NUMBER WITH LIST ELEMENT


l=[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
choice=int(input('enter your lucky number::'))

while True:
    if choice in l:
        print('yes ur lucky number is present')
        break
    #if here we will not write break then it will print(yes ur lucky number is present) infinite
    else:
        print('sry ur lucky number is not present')
        choice=int(input('enter your lucky number again::'))