#date and time:
import datetime
import time
d=datetime.datetime.now()
print(d)

a=time.ctime()
print(a)

b=time.localtime()
print(b)

#short form of day name
c=time.strftime('%a',b)
print(c)

#full form of day  name
d=time.strftime('%A',b)
print(d)

#short form of month name
e=time.strftime('%b',b)
print(e)

#full form of month name
f=time.strftime('%B',b)
print(f)

#short form of year
g=time.strftime('%y',b)
print(g)

#full form of year
h=time.strftime("%Y",b)
print(h)

#hours possible values 1-12
i=time.strftime('%I',b)
print(i)

#day of the year possible values are 0-366
j=time.strftime("%j",b)
print(j)

#hours possible values are 0-23
k=time.strftime('%H',b)
print(k)

#day of the month
l=time.strftime("%d",b)
print(l)

#minutes possible values 0-59
m=time.strftime('%M',b)
print(m)

#seconds possible values 0-59
n=time.strftime("%S",b)
print(n)

#prints am or pm
o=time.strftime("%p",b)
print(o)

#time zone
p=time.strftime("%z",b)
print(p)

#week number of the year
q=time.strftime("%U",b)
print(q)

#century
r=time.strftime("%C",b)
print(r)

s=time.strftime("%x",b)
print(s)

t=time.strftime("%X",b)
print(t)