#search:
#it searches the string for a match,and returns a match object if
#there is a match.
#if there is more than one match only first occurrence will be returned.
import re

text="hello python hello java"
x=re.search("hello",text)
print(x)

#if there is no match found none will be returned.
