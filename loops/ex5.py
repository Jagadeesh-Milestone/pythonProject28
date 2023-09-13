#for loop
#it is used when the user knows exact output
#generally for loop is used on sequences
l=[10,20,30,40]
for number in l:
    print(number)

#break
m=[1,2,3,4,5,6,7]
for i in m:
    print(i)
    if i==5:
        break

#continue
n=[10,20,30,40,50,60]
for i in n:
    if i==40:
        continue
    print(i)
