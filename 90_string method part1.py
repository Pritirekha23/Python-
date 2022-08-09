# string method 
#checking starting and ending of string
s='hello this is python language'
print(s.startswith('Hello'))
print(s.startswith('hello'))
print(s.endswith('age'))
print(s.endswith('Age'))

#chcking what type of char is present in given string
s='hello this is python language'
print(s.isalpha())
   #false bcz space is there

print('isnumeric fun')
s='17698'
print(s.isnumeric())

print('islower fun')
s='python is a popular languagE'
print(s.islower())


print('isalnum fun')
s='156pritI'
s1='1*2'
print(s.isalnum())
print(s1.isalnum())  # * or any mathematical symbols is not allowed 

print('isdigit fun')
s='2333'
print(s.isdigit())


print('isupper fun')
s='TREE'
s1='Tree'
print(s.isupper())
print(s1.upper())


print('istitle function here 1st letter should be capital')
s='Priti'
s1='pRiti'

print(s.istitle())
print(s1.istitle())
print(s1.title())


print('isspace function')
s="   "
s1=" . "
print(s.isspace())
print(s1.isspace())  # . is present so false 
print(type(s))

#changing case
print('upper function --- here it convert all the lower character to upper character')
s='hello this is pRiti'
print(s.upper())
print(s)

print('upper fun ex 2--string is immutable ')
s='Hii how r u'
s1=s.upper()
print(s)
print(s1)
print(id(s))
print(id(s1))


print('lower function --- here it convert all the upper character to lower character')
s='hello this is pRiti'
print(s.lower())
print(s)


print('swapcase function')
s='i am priti Rekha Panda'
print(s.swapcase())


print('title function---here is word 1st letter will be capital')
s='pritiRekha panda'
print(s.title())


print('capitalized function --here a sentence 1st character is capital')
s='pritirekha panda'
print(s.capitalize())



#find out length and count the occurance
print('')
s='hii i am pritirekha panda'
print(len(s))
print(s.count('p'))
print(s.count('a',3))

#replacement of string
print('replacement of string')
s='python is bad programming'
print(s.replace('bad','good'))
print(s)
