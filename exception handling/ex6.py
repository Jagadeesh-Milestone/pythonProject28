#finally:
try:
    a=10
    b=5
    c=0
    print(a/b)
    print('statement one')
except Exception:
    print('statement two')
else:
    print('statement three')
finally:
    print('statement four')
#finally block will be executed even we have errors or no errors.
