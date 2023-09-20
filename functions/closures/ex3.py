def d1():
    l=[10,20,30,40]
    def d2():
        l.reverse()
        return l
    return d2()
d=d1()
print(d)
del d1
print(d)
