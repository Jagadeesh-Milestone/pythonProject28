#plot without line.
#to plot only the markers we can use shortcut string notation "o".
#which means rings.
import matplotlib.pyplot as p
import numpy as np

x=np.array([0,8])
y=np.array([3,10])
p.plot(x,y,'o')
p.show()