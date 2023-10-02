#center:
#it is used to align the string at the center,using a specified character
x="bangalore"
print(x.center(30))
#endswith():
#it is used to check whether the string is ending with the given
#characters
a="Hello python learners"
print(a.endswith('learners'))
#startswith
#it is used to check whether the string is starting with the given
#characters
b="Hello python learners"
print(b.startswith('Hello'))
#\n-new line
#it is used to print in the next line
c="hello\npython\nlearners"
print(c)
#\t-tab space
d="hello\tpython\t\tlearners"
print(d)
#isprintable:
#it returns true if all the characters of a string are printable
e="Hello python@#!\t"
print(e.isprintable())

#join():
#it is used to join the string to a sequence
f=['hello','python','learners']
g="*".join(f)
print(g)

d={'name':'jagadeesh','address':'bangalore'}
e='hello'
f=e.join(d)
print(f)

#split:
#it is used to split the string
h="Hello python hello java"
print(h.split())

i="hello,pyth,on,hel*lo,ja,va"
print(i.split('*'))