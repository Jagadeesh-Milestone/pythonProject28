
def d1(m):
    return m+m
l=[10,20,30,40,50]
x=map(d1,l)
print(list(x))

a=map(lambda c:c*c,l)
print(tuple(a))

for i in l:
    print(i*i)

