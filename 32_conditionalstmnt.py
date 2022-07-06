#input a student mark and check tyhe result
#pass or fail instruction -- mark>=33 pass
# if  (here it will check both condition ,if u want check one condition then this is better)
print('if statement')
mark=int(input('enter u r mark'))
if mark>=33:
    print('pass')  #before print that space is called indentation
if mark<33:
    print('fail') 
#if else(here if the condition is true then it could not check the else contion so it is better than if)
#if u want to chk one condition true and to print false then then it is better
print('if else statement')
mark1=int(input('enter u r mark'))
if mark1>=33:
    print('passs')
else:
    print('fail')
#if elif else
#if u want to chk multiple condition then go for if elif else
print('if elif else')
# 1-a ,2-b,3-c,4-d,5-e other no.--invalid option
n=int(input('enter a number in between 1-5'))
if n==1:
    print('a')
elif n==2:
    print('b')
elif n==3:
    print('c')
elif n==4:
    print('d')
elif n==5:
    print('e')
else:
    print('invalid choice plz chose 1-5')

