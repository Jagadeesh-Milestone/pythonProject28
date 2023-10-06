#hybrid inheritance:
#it is the property in which the combination of more than one type
#inheritance.
class grandparent:
    a='hello world'
    def d1(self):
        print('grand parent property')
        print(self.a)
class parent(grandparent):
    def d2(self):
        print('parent property')
class child(parent,grandparent):
    def d3(self):
        print('child property')
c=child()
c.d1()
c.d2()
c.d3()

p=parent()
p.d1()
p.d2()