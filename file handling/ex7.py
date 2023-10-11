#while in file handling.
x=open('java.txt','w')
name='jagadeesh'
while name=='jagadeesh':
    name=input('enter your name:')
    y=x.write(name)
    print(y)
#the loop will be terminated when you input other than defined name.
