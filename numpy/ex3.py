#accessing elements.
import  numpy as n

x=n.array([10,20,30])
print(x[0])
print(x[-1])
print(x[0]+x[2])

y=n.array([[10,20,30],[40,50,60]])
print(y[0])
print(y[1])
print(y[0,0])
print(y[1,1])

z=n.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
print(z[0,0,0])
print(z[1,1,1])