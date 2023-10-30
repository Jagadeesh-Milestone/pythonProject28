#copy and view:
import numpy as np
x=np.array([10,20,30,40])
y=x.copy()
x[0]=100
print(x)
print(y)

a=np.array([1,2,3,4])
b=a.view()
a[0]=200
print(a)
print(b)
