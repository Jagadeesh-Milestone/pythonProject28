#hirerarchal inheritance
#it is the property in which more than one child classes are derived
#from a single parent class.
class grandparent:
    def d1(self):
        print('grand parent property')
class parent(grandparent):
    def d2(self):
        print('parent propertty')
class child(grandparent):
    def d3(self):
        print('child property')
c=child()
c.d1()
c.d3()

p=parent()
p.d1()
p.d2()