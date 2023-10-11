#file handling:
#in every programming language file handling is the very important
#task.
#we use w,r,a to write,read,append the files.
#writing into a file:
x=open('hello.txt','w')
y=input('enter any value:')
z=x.write(y)
print(z)
x.close()

