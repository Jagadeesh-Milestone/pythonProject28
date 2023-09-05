#sequences
#list
#list is a collection of data and this data may be anytype.
#list allows duplicate values
#list allows index calling and index slicing
#list is mutable meaning that once we create a list we van modify
#the data/values
#list is taken in [] and values are separated by comma
a=[10,10.2,5+6j,True,'bangalore']
print(a)
print(type(a))

#list allows duplicate values
b=[10,20,30,10,20,10]
print(b)

#len()
#it is used to find the no of values in a list
c=[10,20,30,10,20,10]
print(len(c))

#count()
#it is used to find the no of occurrences of a value
c=[10,20,30,10,20,10]
print(c.count(10))
print(c.count(20))
print(c.count(100))

#index()
#the index position of first value is 0,second value is 1...
b=[10,20,30,40,50,60]
print(b.index(60))
#print(b.index(100))
print(b[0])
#print(b[10]

#negative index:
#the index position of last element is -1 before element is -2...
l=[10,20,30]
print(l[-1])
print(l[-2])
#print(l[-6])

#append():
#it is used to add an element at the end of a list
a=[10,20,30,40]
a.append(100)
print(a)

#pop():
#it is used to delete last element from end of a list
b=[100,200,300,150]
#b.pop()
#print(b)
#we can also delete exact element by using index position
b.pop(0)
print(b)

#extend():
#it is used to add multiple values at the end of a list
c=[10,20,30]
c.extend([20,30,40])
print(c)

#insert():
#it is used to insert the values at particular index position
d=[10,30,40,50,60]
d.insert(1,20)
d.insert(10,100)
print(d)