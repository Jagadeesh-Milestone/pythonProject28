#variables
#there are three types of variables
#global variables
#local variables
#protected variables
#global variables:
#once we declare a variable globally we can access it anywhere
#throughout the program
x=100
print('x value before the function:',x)
def d1():
    print('x value inside the function:',x)
d1()
print('x value after the function:',x)

