#global keyword
#it is used to access local variable outside the function(globally)
x=100
print('global x value is:',x)
def d1():
    global x
    x=200
    print('local x value is:',x)
d1()
print('local x value is:',x)