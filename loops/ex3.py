#break
#it is used to break the loop at a particular condition
i=0
while i<10:
    print(i)
    if i==4:
        break
    i+=1

m=0
text="hi python learners"
while m< len(text):
    if text[m]=='l' :
        m+=1
        break
    print(text[m])
    m+=1
