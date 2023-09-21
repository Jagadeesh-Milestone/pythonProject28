#multiple expressions
def d1(a,b,c,d):
    print(a+b)
    print(c-d)
    print(a*d)
    print(b/c)
d1(10,20,30,40)

#using lambda:
x=lambda a,b,c,d:(a+b,a-b,c*d,d/a)
print(x(10,20,30,40))