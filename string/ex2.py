#string methods
x="heLlo worLD"
print(x)
#upper:
#it returns all the characters of a string in upper case
print(x.upper())
#lower:
#it returns all the characters of string in lower case
print(x.lower())
#title:
#it returns first letter of every word in upper case
print(x.title())
#swapcase:
#it returns all upper case letters in lower case and vice versa
print(x.swapcase())

#is upper:
#it returns true if all the characters of a string are in upper case
#otherwise it returns false
a="BANGALORE"
print(a.isupper())

#is lower:
#it returns true if all the characters of a string are in lower case
#otherwise it returns false
b="hyderabad"
print(b.islower())

#is title:
#it returns true if first character of every word in a string is
#upper case and remaining in lower case else it returns false
c="Hello Python"
print(c.istitle())

#strip:
#it is used to remove whitespaces in a string
d=" Hello "
print(len(d))
print(d)
print(d.strip())
#lstrip:
#it is used to remove left white space
print(d.lstrip())
#rstrip:
#it is used to remove right white space
print(d.rstrip())

#replace:
#it is used to replace a character with other
e="Hello World Hello Python"
print(e.replace('l','jagadeesh'))
print(e.replace('l','python',2))
#we can put limit for the replace

#is space:
#it returns true if a string has only space else it returns false
f="  "
print(f.isspace())
g=" hello    "
print(g.isspace())

#is numeric:
#it returns true for only numbers in a string else false
h="10"
i="10.2"
j="hello"
k="10+5j"
print(h.isnumeric())
print(i.isnumeric())
print(j.isnumeric())
print(k.isnumeric())

#is decimal:
#it returns true only for numbers in a string
print(h.isdecimal())
print(i.isdecimal())
print(j.isdecimal())
print(k.isdecimal())

#is digit:
#it returns true only for numbers in a string
print(h.isdigit())
print(i.isdigit())
print(j.isdigit())
print(k.isdigit())

#is alpha:
#it returns true if a string contains only alphabets
l="Helloworld"
print(l.isalpha())

#is alnum:
#it returns true if a string contains alphabets or numbers or both
m="Hello56565"
n="Hello"
o="632556"
print(m.isalnum())
print(n.isalnum())
print(o.isalnum())
#max()
x="hyderabad"
print(max(x))
print(min(x))

l=[10,20,30,5,4,]
print(max(l))
print(min(l))

#capitalize:
x="hello world"
print(x.capitalize())