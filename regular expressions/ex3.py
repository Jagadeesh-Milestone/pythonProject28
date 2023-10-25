import re
text="hello python hello java"
x=re.findall("^hello",text)
print(x)
#^ is used to check whether the string is starting with the specified
#characters or not.

y=re.findall("java$",text)
print(y)
#$ is used to check whether the string is ending with the specified
#characters or not.