#returning a value/expression
def d():
    return 'hello world'
print(d())

#returning a function
def d1():
    def d2():
        return 'hello milestone'
    return d2()
d=d1()
print(d)