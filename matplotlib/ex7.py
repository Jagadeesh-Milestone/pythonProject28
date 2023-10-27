#multiple lines
import  matplotlib.pyplot as p
import numpy as np

x=np.array([12,14,16,17])
y=np.array([2,4,6,8])
z=np.array([3,7,10,15])
p.plot(x,'d-r')
p.plot(y,'d-b')
p.plot(z,'o:g')
p.show()