#set
#set is collection of data and this data may be anytype
#set dont allow index calling,index slicing and duplicate values
#set is taken in {}
#set is having unordered elements
#set is mutable
s={10,10.0,5+6j,True,100}
print(s)
print(type(s))

#set dont allow index calling
#a={10,20,30,40}
#print(a.index(10))

#set dont allow duplicate values
b={10,20,30,10,20,10}
print(b)

#add
c={100,200,300}
c.add(300)
print(c)

#update
d={10,20,40,60}
d.update([300,500])
print(d)

#remove():
e={100,200,300,400}
e.remove(200)
print(e)

#discard():
f={10,20,30,40}
f.discard(20)
print(f)

#difference between remove and discard
g={10,20,30,100,200,300}
#g.remove(1000)
#print(g)
g.discard(1000)
print(g)

#pop():
h={10,20,30,40,50}
h.pop()
print(h)

#clear():
i={1,2,3,54}
i.clear()
print(i)

#union():
j={10,20,30,40}
k={50,40,60,70}
print(j.union(k))

#intersection:
j={10,20,30,40}
k={50,40,60,70,20}
print(j.intersection(k))

#difference():
j={10,20,30,40,50,60,70}
k={50,40,60,70}
print(j.difference(k))

#subset()
l={10,20,30}
m={10,20,30,40,50}
print(l.issubset(m))

#superset():
l={10,20,30,40,50}
m={10,20,30}
print(l.issuperset(m))