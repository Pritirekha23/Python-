# WHAT IS  DEFAULT ARGUMENT
 #Default argument means optional argument.
 #In default argument at the time of function calling if we not pass argumrnt then it will considerthe default value.



def fun(name):
    print(f'hi{name} good morning')
fun('priti')
#fun() #TypeError: fun() missing 1 required positional argument: 'name' --- how to make it default that is the main here

print('default argument example-1')
#it will take unknown as default value
def fun(name='unknown'):
    print(f'hi{name} good morning')
fun()

print('default argument example-2')
def fun(name='unknown'):
    print(f'hi {name} good morning')
#if u pass any value then it will give more priority than default value .
fun('priti')



# WORKING WITH POSITIONAL ARGUMENT AND DEFAULT ARGUMENT
#we can make both as optional
print('working with positional and default argument ex-1')
def msg(bf='u dont have bf',gf='u dont have gf'):
    print(f'hi {bf}  your girlfriend is {gf}')


msg('Jungkook','jin')
msg('Kim namzoon')   # here 2nd value is not given so it will take the default value
msg()
msg(gf='yuu')



#NOTE-
  # write default argument after non-default argument
  #or
    # we cant write non-default argument after default argument

#SyntaxError: non-default argument follows default argument

#def student(name,id,email='no email',mark):
    #555 is trying to store in email ,the email is not purely default
   # print('name is',name)
   # print('id is',id)
   # print('mark is',mark)

#student('priti',156,555)

print('write default argument after non-default argument')
def student(name,id,mark,email='no mail'):
    #555 is trying to store in email ,the email is not purely default
        print('name is',name)
        print('id is',id)
        print('mark is',mark)
        print('email is',email)

student('priti',156,555)



def student(name,id,mark,email='no mail',addr='no'):
        print('name is',name)
        print('id is',id)
        print('mark is',mark)
        print('email is',email)
        print('addr is',addr)


student('priti',156,555,'panda2222@gmail.com','Bhadrak')

def student(name,id,mark,email='no mail',addr='no'):
        print('name is',name)
        print('id is',id)
        print('mark is',mark)
        print('email is',email)
        print('addr is',addr)


student('priti',156,555,addr='Bhadrak')

#this bhadrak will store email na so better to write keyword argument





















