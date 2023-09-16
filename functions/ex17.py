
def d1(a,b):
    return 'hello world',a,b
def d2(c):
    return 'hello python',c
def d3():
    return 'hello milestone'
d=d1(d2(d3()),d3())
print(d)

d=d2(d3())
print(d)