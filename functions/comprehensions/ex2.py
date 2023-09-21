#list comprehension
users=['hari','mahesh','suresh','chandu']
x=[]
for i in users:
    if 'sh' in i:
        x.append(i)
print(x)

#using list comprehension
x=[i for i in users if 'sh' in i]
print(x)