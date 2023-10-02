a="I have {:<10} mangos"
b=a.format(500)
print(b)

c='I have {:>10} bananas'
d=c.format(20)
print(d)

e='I have {:^10} cherrys'
f=e.format(200)
print(f)

g="I have {:,} rupees"
h=g.format(1000000)
print(h)

i='I have {0:b} apples'
j=i.format(5)
print(j)

k="I have {:d} kites"
l=k.format(0b101)
print(l)

m="I have {0:x} grapes"
n=m.format(18)
print(n)

o="i have {:d} rupees"
p=o.format(0x12)
print(p)

q="I have {0:o} rupees"
r=q.format(8)
print(r)

s="mango"
print(s.ljust(20,'o'))

t="banana"
print(t.rjust(20,'z'))
