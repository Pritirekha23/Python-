#How to iterate nested dictionary 
students={
    156:{'name':'priti','email':'pandapriti@gmail.com','mob':334455667788},
    172:{'name':'shivani','email':'shivani@gmail.com','mob':934889998},
    195:{'name':'laxmi','email':'laxmi@gmail.com','mob':88887788}
}
for k,v in students.items():
    print('student id is : ',k)

    for i in v:
        print(f'{i} is : {v[i]}')
    
    print('-'*30)