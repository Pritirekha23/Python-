# wap to read the number untill -1 entered also count the negative,possitive and zeros entered the user
num=int(input('enter a number(if u want to exit then enter -1)'))
np=0
nn=0
nz=0
while num!=-1:
    if num>0:
        np=np+1
    elif num<0:
        nn=nn+1
    else:
        nz=nz+1
    num=int(input('enter a number(if u want to exit then enter -1)'))
print('number of posiitive',np)
print('number is negative',nn)
print('number is zero',nz)