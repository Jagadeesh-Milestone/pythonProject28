#sequences
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