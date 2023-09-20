#decorators
#these are the higher order functions
#these are used to add an extra functionality to another function
#we use @ annotation as a decorator
#function without decorator:
def d1(func):
    def d2():
        result=func
        return result+"world"
    return d2()
def d3():
    return 'Hello'
d=d1(d3())
print(d)
del d1
print(d)
