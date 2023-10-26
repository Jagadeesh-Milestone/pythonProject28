#sub:
#it is used to replace the string with the match object.
import re

text="hello python learners"
x=re.sub('l','jagadeesh',text)
print(x)

y=re.sub('l','hari',text,2)
print(y)