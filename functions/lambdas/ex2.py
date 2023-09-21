#default arguments
#x=lambda a,b=20:a+b
#print(x(40))
#print(x(100,200))

#nested lambda:
x=lambda a:(lambda b=30:a+b)
y=x(100)
print(y())

