#create labels:
import pandas as p

x=[10,20,30,40]
y=p.Series(x,index=['a','b','c','d'])
print(y)
print(y['a'])