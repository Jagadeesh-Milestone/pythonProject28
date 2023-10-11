#pickling:
#it is the process of converting python object to byte stream code
#we use dump method in pickling
#to use pickle we have to import it.
import pickle
x=open('html.dat','wb')#wb-write bytes #dat--data file
a=[10,20,30,40]
y=pickle.dump(a,x)
print(y)
x.close()
