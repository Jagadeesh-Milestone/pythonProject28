#numpy array iterating:
#we use for loop for iterating over the numpy arrays
import numpy as np
x=np.array([10,20,30])
for i in x:
    print(i)

y=np.array([[1,2,3],[4,5,6]])
print(y)
for i in y:
    for m in i:
        print(m)

z=np.array([[[10,20,30],[40,50,60]],[[70,80,90],[100,110,120]]])
print(z)
for i in z:
    for a in i:
        for b in a:
            print(b)