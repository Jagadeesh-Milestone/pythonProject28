#frozenset
#it is the immutable version of set,list
a={10,20,30,40}
b=frozenset(a)
print(b)
print(type(b))

#b.add(200)
#print(b)

c=[10,20,40,50]
d=frozenset(c)
print(d)
print(type(d))
d.append(100)
print(d)
