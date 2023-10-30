#numpy datatypes:
import numpy as np

x=np.array([1,2,3,4])
print(x.dtype)

y=np.array(['hello','python','apple'])
print(y.dtype)

z=np.array([True,False])
print(z.dtype)

#convert datatype another datatype:
a=np.array([10,20,0,30,10,0,0],dtype=bool)
print(a)

b=np.array([10.3,10.6,11.2],dtype=int)
print(b)