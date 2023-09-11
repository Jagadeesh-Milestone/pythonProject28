#identity operators
#it returns true if the ids of two objects are same
a=10
print(a)
print(id(a))
b=10
print(id(b))
a=30
print(id(a))

l=[10,20,30,40,50]
m=[10,20,30,40,50]
n=l
print(id(l))
print(id(m))
print(id(n))
print(l is m)
print(m is n)
print(l is n)
print(l is not m)
print(m is not n)
print(l is not n)