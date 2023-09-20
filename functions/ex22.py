#globals method():
#it is used to access the global variable locally when the both
#global and local variables having same name.
x=100
print('global x value:',x)
def d1():
    x=200
    print('local x value:',x)
    print('global x value:',globals()['x'])
d1()
print('x value after the function',x)

