#scope
#there are two types of scopes
#global scope
#local scope

#global scope
#we can use arguments of outer function inside the inner function
def d1(a,b):
    print(a+b)
    message='hello world'#global scope variable
    print(message)
    def d2():
        print(a*b)
        print(message)
    d2()
    print(message)
    print(a*b)
d1(10,20)
#print(message)#d1 scope ended

