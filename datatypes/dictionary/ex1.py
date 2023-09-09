#dictionary
#empty dictionary:
a={}
print(a)
print(type(a))

#dictionary
b={'name':'hari','address':'bangalore','contact':9808980989}
print(b)
print(type(b))
#keys
print(b.keys())
#values
print(b.values())
#items
print(b.items())

#add
b['age']=27
print(b)
#update
b['address']='hyderabad'
print(b)

#pop():
#b.pop('name')
#print(b)

b.popitem()
print(b)

#constructing a dictionary:
x=dict(name='jagadeesh',address='bangalore',contact=989998899)
print(x)

#dupilcate keys are not allowed
d={'name':'jagadeesh','name':'hari'}
print(d)

#duplicate values are allowed
a={'name1':'hari','name2':'hari'}
print(a)

#delete a key:
b={'name':'suresh','address':'bangalore'}
del b['name']
print(b)
#del b['bangalore']#we cant delete the values directly
#print(b)
#deleting a dictionary
#del b
#print(b)

#len()
x=dict(name='jagadeesh',address='bangalore',contact=989998899)
print(len(x))

#accessing elements
print(x['address'])
a=x.get('contact')
print(a)