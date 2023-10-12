#try and except:
try:
    a=10
    b=5
    c=0
    print(a/b)
    print('statement one')
    print(b/c)
except ZeroDivisionError:#to except one type of error.
    print('statement two')