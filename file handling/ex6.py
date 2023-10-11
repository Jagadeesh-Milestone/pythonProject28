#tell():
x=open('hello.txt','r')
print(x.read())
#print(x.tell())
#print(x.read(10))
#print(x.tell())
#10 values will be printed remaining will not be printed.

#seek:
print(x.seek(10))
print(x.read())
#10 values will be seeked and remaining will be printed
