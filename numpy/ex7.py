#array shape
import numpy as np

x=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(x.shape)

#reshape:
y=np.array([[1,2,3,4],[5,6,7,8]])
print(y.reshape(4,2))

z=np.array([1,2,3,4,5,6,7,8,9,10])
print(z.reshape(5,2))