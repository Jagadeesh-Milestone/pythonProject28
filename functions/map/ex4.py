l=[1,2,3,4,5,6,7,8]
for i in l:
    if i%2==0:
        print(i*3)
    else:
        print(i)

#using map:
def d1(x):
    if x%2==1:
        return x*5
    else:
        return x
a=map(d1,l)
print(list(a))

