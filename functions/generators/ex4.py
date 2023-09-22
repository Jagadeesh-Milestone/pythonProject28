
def d1(n):
    for i in range(n):
        yield i
d=d1(3)
#print(next(d))
#print(next(d))
#print(next(d))

for i in d:
    print(i)