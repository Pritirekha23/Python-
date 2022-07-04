#1
c=50+20j
print(type(c))
print(c)
#2
c=23.22+10j
print(c)
#3
c=45.69+88.96j
print(c)
#4 we can set all type of value(bin/oct/hex/dec) in real part  but we cant use these values in imaginary part except decimal
c=0o6542+8j
print(c)
#5
c=0x342abcd+3j
print(c)
#6
c=30+2.2j
print(c)
#7 error producing bcz (#4)
c=30+0b111j
print(c)