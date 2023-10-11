#unpickling:
#it is the process of converting byte stream code to python object
#we use load method in unpickling:
import pickle
x=open('html.dat','rb')#rb--read bytes.
y=pickle.load(x)
print(y)
x.close()
