#sequences
#list
#a list is a collection of data and this data may be any type
#list is taken in []
#list is having ordered elements
#list allows duplicate values,index calling and index slicing
#list is mutable meaning that we can change the values
l=[]
print(l)
print(type(l))

a=[10,10.0,5+6j,True,'bangalore',[10,20,30]]
print(a)
print(type(a))

#len():
#it is used to find the no of values in a list
b=[10,20,30,40]
print(len(b))

#count():
#it is used to find the no of appearances of an element.
c=[10,20,30,10,20,10]
print(c.count(10))
print(c.count(100))

#duplicates are allowed
d=[10,20,10,20,10]
print(d)

#append()
#it is used to add an element at the end of a list
e=[100,200,300]
e.append(400)
print(e)

#index position:
#the index position of first element is 0,second is 1,...
f=[10,20,30,40,50]
print(f.index(10))
print(f.index(50))
#print(f.index(100))
#finding the value in a particular index position
print(f[0])
print(f[4])
#print(f[5])
#Negative index:
#the negative index position is from right to left
#the index position of last element is -1 and -2,...
print(f[-1])
print(f[-5])
#print(f[-6])

#pop():
#it is used to remove last element from the list:
l=[10,20,30,40]
#l.pop()
#print(l)

#we can remove particular element by using index position in pop
l.pop(-1)
l.pop(0)
print(l)

#extend():
#it is used to add multiple values at the end of  a list
a=[100,200,300]
a.extend([10,20,30])
print(a)

#insert():
#it is used to insert an element at particular index position
b=[10,20,40,50,60]
b.insert(2,[30,40,50])
b.insert(2,30)
print(b)

#copy():
#it is used to copy the list elements
c=[10,20,30,40]
d=c.copy()
print(d)

#clear():
#it is used to clear the list elements
e=[100,200,300]
e.clear()
print(e)

#remove():
#it is used to remove an element from the list
f=[1,2,3,4,5]
f.remove(3)
print(f)

#reverse():
#it is used to reverse the list of elements
g=[10,40,30,20,50]
g.reverse()
print(g)

#sort():
#it is used to print the elements in ascending or descending order
h=[10,40,30,20,50]
h.sort(reverse=False)
print(h)

h.sort(reverse=True)
print(h)


