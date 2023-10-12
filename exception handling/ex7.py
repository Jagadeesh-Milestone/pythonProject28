#raise an exception:
#we can create our own errors using raise keyword:
a=10.9
if type(a) is not int:
    raise Exception('enter only integers')
print(a)

b=int(input('enter a number:'))
if b<0:
    raise ('enter only positive values')
print(b)