#multi level inheritance:
#it is the property in which more than one child class and one parent
#class.
class grandparent:
    def d1(self):
        print('grand parent property')
class parent(grandparent):
    def d2(self):
        print('parent property')
class child(parent):
    def d3(self):
        print('child property')
c=child()
c.d1()
c.d2()
c.d3()

p=parent()
p.d1()
p.d2()

