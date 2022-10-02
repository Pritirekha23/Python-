# dt-16-09-22
# wap to create a strong password
import random as ra

alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
digits='0123456789'
sp_symbol="~!@#$%^&*()_+[]<>/|"

print(ra.choice(alpha+digits),ra.choice(digits+sp_symbol),ra.choice(sp_symbol+alpha),ra.choice(alpha),ra.choice(digits),ra.choice(sp_symbol+alpha),sep='')