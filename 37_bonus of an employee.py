#A company decides to give bonus to its employee on this diwali
# A 5% bonus on salary is given to the male workers and 10% bonus salary to the female workers.
# if salary of the employee is less than 15000 then the employee get an extra 3% bonus of the salary.
#WAP to enter your salary and gender then calculate the bonus that has to given to the employee and display the salary that the employee will get
s=int(input('enter employee salary'))
g=input('enter your gender')

if g=='m':
    bonus=0.05*s
else:
    bonus=0.10*s
if s<15000:
    print('u will get extra 3% bcz sal<15000')
    bonus=bonus+0.03*s
s=bonus+s
print('sal is',s)