import jagadeesh
from jagadeesh import  d1,d2,user
d=jagadeesh.d1('python learners')
print(d)

x=d1('java learners')
print(x)

y=d2('html learners')
print(y)

z=jagadeesh.d2('sql learners')
print(z)

print(dir(jagadeesh))

a=user
print(a.keys())
print(a.values())

b=jagadeesh.user
print(b['name'])
