#index slicing:
import numpy as np
x=np.array([10,20,30,40,50])
print(x[0:3])
print(x[0:4:2])
print(x[2:])
print(x[:])

y=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(y[0,1:4])
print(y[1,0:4:2])
print(y[1,1:4])

z=np.array([[[1,2,3,4]],[[5,6,7,8]]])
print(z[0,0,0:3])

