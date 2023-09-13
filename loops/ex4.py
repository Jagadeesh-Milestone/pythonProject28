#continue
#it is used to skip the current condition and continue with the others
i=10
while i<20:
    i+=1
    if i==16:
        continue
    print(i)

n=0
text="hello python learners"
while n< len(text):
    if text[n]=='l' or text[n]=='e':
        n+=1
        continue
    print(text[n])
    n+=1