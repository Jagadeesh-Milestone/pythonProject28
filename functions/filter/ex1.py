#filter
x=[1,2,3,4,5,6]
for i in x:
    if i%2==0:
        print(i)

def d1(a):
    return a%2==1
f=filter(d1,x)
print(list(f))

x=filter(lambda b:b%2==0,x)
print(tuple(x))