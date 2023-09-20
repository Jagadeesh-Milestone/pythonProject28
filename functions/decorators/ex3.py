
def d1(func):
    def d2(a):
        return func(a*a)
    return d2
@d1
def d3(a):
    return a
print(d3(10))
