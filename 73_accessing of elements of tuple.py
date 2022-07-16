# we can access tuple elements by using index and slice operator

#ACCESSING BY USING INDEX
print(' ACCESSING tuple BY index')
t=(5,56,7,8)
print(t[3])
print(t[1])
print(t[-2])
# print(t[66]) # type error bcz 66 index is not present in the tuple


# ACCESSING BY SLICE OPEARATOR
print(' ACCESSING tuple BY SLICE OPEARATOR')
t=(5,56,7,8)
print(t[::])
print(t[::1])
print(t[:1:2])
print(t[::2])