#marker size and marker color:

import  matplotlib.pyplot as p
import  numpy as np
x=np.array([2,3,4,5,6])
y=np.array([10,12,13,17,19])
p.plot(x,y,'D:g',ms=6,mfc='violet')
p.show()

#ms--marker size
#mec--marker edge color--color at marker edges
#mfc--marker face color--color inside the marker
#we can use both mec and mfc at a time
