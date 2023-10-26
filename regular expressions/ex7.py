#split:
#it is used to split a string at each match.
import re

text="hello python hello java"
x=re.split("l",text)
print(x)

y=re.split('l',text,2)
print(y)
