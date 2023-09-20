#normal function
def d1():
    print('hello world')
d1()
#del d1
#d1()#we cant use the normal function after it is deleted.
#use of closure:
#after the deletion of actual function we can use its functionality
def d2(a,b):
    def d3():
        return a+b
    return d3()
d=d2(10,30)
print(d)
del d2
print(d)
print(d)