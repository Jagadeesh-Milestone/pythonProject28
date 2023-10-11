#add into existing file:
x=open('hello.txt','a')
y=x.write('hello html learners')
print(y)
x.close()

#if we use 'w' instead of 'a' the data in the file will be overwritted.