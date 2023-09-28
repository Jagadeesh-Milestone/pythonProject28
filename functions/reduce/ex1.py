#reduce:
from functools import reduce
import functools
x=[10,20,30,40,50]
print(x+x)

for i in x:
    print(i+i)

def d1(m,n):
    return m+n #10(m)+20(n)=30(m)+30(n)=60(m)+40(n)=100(m)+50(n)
x=reduce(d1,x)
print(x)