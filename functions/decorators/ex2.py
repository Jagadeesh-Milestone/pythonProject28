#using decorator
def d1(func):
    def d2():
        result=func()
        return result+"learners"
    return d2()
@d1
def d3():
    return "hello python"
d=d3
print(d)