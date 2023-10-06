#multiple inheritance.
#it is the property in which a single child class is deriving from
#more than one parent class.
class grandparent:
    def d1(self):
        print('grand parent property')
class parent:
    def d2(self):
        print('parent property')
class child(grandparent,parent):
    def d3(self):
        print('child property')

c=child()
c.d1()
c.d2()
c.d3()

p=parent()
p.d2()