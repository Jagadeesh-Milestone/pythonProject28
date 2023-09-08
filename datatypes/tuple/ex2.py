#converting a tuple to list:
t=(10,20,30,50)
a=list(t)
print(a)
print(type(a))
a.append(100)
print(a)

#converting a list to tuple:
b=[100,200,300,400]
c=tuple(b)
print(c)
print(type(c))
c.append(500)
print(c)