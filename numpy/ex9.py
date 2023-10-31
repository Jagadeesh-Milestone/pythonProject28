#nditer:

import numpy as np
x=np.array([[10,20,30,40],[50,60,70,80]])
for i in np.nditer(x):
    print(i)
print('hello world')
for a in np.nditer(x[: ,::2]):
    print(a)