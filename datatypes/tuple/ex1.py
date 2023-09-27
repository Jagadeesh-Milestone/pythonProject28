#tuple:
#it is a collection of data and this data may be any type:
#it is taken in parenthesis()
#it is immutable means we cant change the values/data/items
#it allows duplicate values,index calling,index slicing

t=(10,20,30,40)
print(t)
print(type(t))

#it allows duplicate values
a=(10,20,10,20,10)
print(a)

#it allows index calling
b=(10,20,30,40)
print(b.index(10))
print(b[2])
print(b[-2])
#print(b[-10])

#len():
c=(10,20,30,40)
print(len(c))

#count():
d=(1,2,3,1,2,1)
print(d.count(1))
print(d.count(100))

#concatenation:
#adding one tuple to another tuple or a list to list is called
#concatenation
e=(1,2,3,4,5)
print(e+(6,7,8,1))

#repetetion
f=(10,20,30)
print(f*3)

g=(10)
print(g)
print(type(g))

h=(10,)
print(h)
print(type(h))