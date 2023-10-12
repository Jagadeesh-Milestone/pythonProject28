#multiple exceptions
try:
    a=[10,20,30,40]
    print(a.index(10))
    print('statement one')
    print(a.index(100))
    b={10,20,30,40}
    print(b[10])

except Exception:
    print('statement three')


