#comprehensions
#these are used to concise the code
#these are used to create a new sequence from existing sequence
l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    if i%2==0:
        print(i,'is an even number')
    else:
        print(i,'is an odd number')
#using list comprehensions
x=[i for i in l if i%2==0]
print(x)
