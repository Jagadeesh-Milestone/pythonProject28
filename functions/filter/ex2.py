l=['a','b','c','d','e','f','g','a','e','i']
vowels=['a','e','i','o','u']
for i in l:
    if i in vowels:
        print(i)

def d1(m):
    if m in vowels:
        return m
f=filter(d1,l)
print(list(f))

