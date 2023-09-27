a=['bangalore','mumbai','hyderabad','chennai']
print(len(a))
#using for loop
for i in a:
    print(len(i))

#using map
def d1(m):
    return len(m)
x=map(d1,a)
print(list(x))

#using lambda:
y=map(lambda n:len(n),a)
print(tuple(y))

a=['bangalore','mumbai','hyderabad','chennai']
#a.reverse()
#print(a)
#using for loop
for i in a:
    print(i[::-1])

#using map:
def d1(c):
    return c[::-1]
d=map(d1,a)
print(list(d))

#using lambda:
e=map(lambda f:f[::-1],a)
print(tuple(e))

