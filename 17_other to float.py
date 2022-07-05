#B
#other to float is possible except complex and str must contain int or float value
#other to float
#1  int to float
k1=float(22)
print(k1)
#2 bool to float
#
k2=float(True)
print(k2)
k3=float(False)
print(k3)
#
k4=float(False+True+True*True)
print(k4)
 #3 str to float
 # possible ,it is possible here bcz it is float
k6=float('12.4')
print(k6)
# not possible
k5=float('priti')
print(k5)
#4 complex to float
#error
k7=float(13+3j)
print(k7)