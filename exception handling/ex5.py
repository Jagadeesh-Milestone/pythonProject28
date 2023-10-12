#else:
try:
    l=[10,20,30,40]
    print(l.index(10))
    print('hello world')
except Exception:
    print('exception statement')
else:
    print('else statement')
#if there is an error exception statement will be printed
#if there is no error else statement will be printed