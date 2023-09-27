l=[10,20,30,40,50]
s=[1,2,3,4]
#print(l*s)#50 dont have any mapping element in s.so it will not
#be printed.

#using map
def d1(x,y):
    return x*y
m=map(d1,l,s)
print(list(m))

#using lambda:
n=map(lambda a,b:(a+b),l,s)
print(list(n))