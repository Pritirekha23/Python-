msg="welcome to python"
slice(1,12,2)
print('hlo')
print(msg[1:12:2])

print('hihi')
print(msg[3:15:2])
print(msg[::])
print(msg[::2])
print(msg[:5000:2])

print('start val is specified but not present')
print(msg[100:12:2])
print('anything')
print(msg[::-1])
print(msg[::-2])
print(msg[-15:-14:-1])
print(msg[8:15:-1])
print(msg[5000:2:-1])
print(msg[-6::])
print(msg[-1:-4:-1])
print(msg[:-4:])
print(msg[-4:-1:])
print(msg[2:9])
print(msg[2:])
print(msg[::+-1])
print(msg[1:-12:])
print(msg[-2:-12:])
print(msg[True:-1:-1])
print(msg[False+10:(True-True):-1])
print(msg[200:2:2])
print(msg[500:2:2])

#Syntax

# arr[start:stop]         # items start through stop-1
# arr[start:]             # items start through the rest of the array
# arr[:stop]              # items from the beginning through stop-1
# arr[:]                  # a copy of the whole array
# arr[start:stop:step]    # start through not past stop, by step