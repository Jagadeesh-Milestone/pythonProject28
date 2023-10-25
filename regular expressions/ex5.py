import re

text="hello 78 python 3 hello 56 java 3"
x=re.findall('[0-9]',text)
print(x)
#it returns all the digits between 0-9

y=re.findall('[038]',text)
print(y)
#it returns if a string contains any 0,3,8 digits