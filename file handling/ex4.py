#writelines:
x=open('python.txt','w')
y=['bangalore','chennai','hyderabad']
z=x.writelines(y)
print(z)
x.close()
