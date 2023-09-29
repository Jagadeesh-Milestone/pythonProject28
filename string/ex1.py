#string
#a string is a collection/sequence of characters
x="bangalore"
print(x)
print(type(x))
print(len(x))
print(x.count('a'))
y=reversed(x)
print(list(y))
for i in y:
    print(i)
print(x[::-1])

for i in reversed('hyderabad'):
    print(i)

#slicing
y="milestone"
print(y[0])
print(y.index('n'))
print(y[2:9])

z='bangalore'
print(z.index('a'))
print(z.rindex('a'))

#string concatenation
a="banaglore"
b="hyderabad"
print(a+b)
print(a+"chennai")

#string repetition
print(a*3)

#combining with + operator
print('a'+'b'*6+'c')
print(('a'+'b')*7+'c')

