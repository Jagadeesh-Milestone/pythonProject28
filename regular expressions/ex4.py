
import re

text="hello python learners"
x=re.findall("[a-m]",text)
print(x)
#it returns the characters of a string between a-m

y=re.findall("[^a-m]",text)
print(y)
#it returns the characters otherthan a-m