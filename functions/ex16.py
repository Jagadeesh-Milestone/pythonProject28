#function as an argument
#we can pass a function as a value to an argument

def d1(a):
    return 'hello world',a
def d2():
    return 'hello milestone'

d=d1(d2())
print(d)