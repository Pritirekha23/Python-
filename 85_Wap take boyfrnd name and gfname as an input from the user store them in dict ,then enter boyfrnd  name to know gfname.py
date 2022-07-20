#85_Wap take boyfrnd name and gf name as an input from the user store them in dict ,then enter boyfrnd  name to know gf name .

d={}
while True:
    bf=input('Enter bf name::')
    gf=input('Enter your gf name::')
    d[bf]=gf
    choice=input('Do u want to more item[y/n]')
    if choice=='n':
        break
while True:
    bf=input('enter your bf name to get gf name::')
    gf=d.get(bf,0)
    if gf==0:
        print('sry bf name is not available')
    else:
        print(f'Hi {bf} your gf name is {gf}') 
    choice=input('do u want to search more items[y/n]')
    if choice=='n':
        break