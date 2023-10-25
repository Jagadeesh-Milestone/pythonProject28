#findall
#it returns a list containing all the matches.
import re
text="hello world hello python"
x=re.findall("hello",text)
print(x)

y=re.findall("java",text)
print(y)
#if there were no match then empty list will be displayed.
