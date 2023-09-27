#map
#it is the builtin function
#it returns the sequence with the map object
l=[1,2,3,4,5,6,7,8]
print(l*3)#entire list is printing three times
#using for loop
for i in l:
    print(i*3)

#using map function
def d1(a):
    return a*5
m=map(d1,l)
print(tuple(m))#here we are getting multiple values so we
#convert map object into a sequence

#using lambda
x=map(lambda b:b*10,l)
print(list(x))
