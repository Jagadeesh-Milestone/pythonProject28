#generator
def d1():
    yield 100
    yield 200
    yield 300
print(d1())
d=d1()
print(next(d))
print('hello world')
print(next(d))
print(next(d))
print(next(d))