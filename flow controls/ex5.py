l=10
m=[10,20,30,40,50]
if l in m:
    print('l is in list')
else:
    print('l is not in list')

x='100'
if not type(x) is int:
    print('x is not an integer,it is',type(x))
else:
    print('x is an integer')

password=int(input('enter your password'))
if password>999 and password<9999:
    print('password is correct')
else:
    print('password must be four digits')

if password<1000 or password>9999:
    print('password must be four digits')
else:
    print('password is correct')