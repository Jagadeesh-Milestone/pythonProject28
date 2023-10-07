#polymorphism.
#it is the property in which same method having many forms.
#polymorphism in * operator:
#* operator in multiplication
a=10
b=20
print(a*b)

#* operator in power.
c=4
d=5
print(c**d)

#* operator in sequence repetition
l=[10,20,30]
print(l*3)

#* operator in args
def d1(*students):
    print(students)
d1('hari','manoj','suresh')

#* operator in kwargs
def d2(**employee):
    print(employee)
d2(emp1='hari',emp2='naresh')

