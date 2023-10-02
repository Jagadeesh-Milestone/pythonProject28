#format
#it is used to format the string with the new string
x="my name is {} my address is {}"
y=x.format('jagadeesh','bangalore')
print(y)

a='my name is {0} my address is {1}'
b=a.format('hari','bangalore')
print(b)

c='my name is {name} my address is {address}'
d=c.format(name='mahesh',address='hyderabad')
print(d)