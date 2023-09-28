ages=[10,23,12,19,21,28]
for i in ages:
    if i>21:
        print(i,'is eligible for vote')

def d1(m):
    if m>21:
        return m
x=filter(d1,ages)
#print(list(x),'are eligible for vote')
for i in x:
    print(i)

c=filter(lambda d:d>21,ages)
#print(list(c))
for i in c:
    print(i)