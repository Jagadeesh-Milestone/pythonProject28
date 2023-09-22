#dict comprehensions
d={}
l=[10,20,30,40,50]
for i in l:
    d[i]=i*5
print(d)

#using dict comprehension
x={i:i*2 for i in l }
print(x)