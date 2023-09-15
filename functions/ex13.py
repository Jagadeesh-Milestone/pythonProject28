#nested function with arguments
#we can use return statement in outer function or inner function
#but we cant use return statement in both the functions
def d1(a,b):
    print(a+b)
    def d2(c,d):
        return c*d
    print(d2(5,6))
d1(10,20)
