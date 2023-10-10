#encapsulation:
#it is the property in which wrapping up of attributes and methods
#into a single entity is called encapsulation.
class parent:
    def __init__(self):
        self._a=100
        self._b=300
    def d1(self):
        self._d=1000
class child(parent):
    def __init__(self):
        parent.__init__(self)
        print('parent attribute:',self._a)
        print('parent attribute:',self._b)
        parent.d1(self)
        print('d1 attribute',self._d)
    a=200
    print('child attribute,',a)
c=child()
print(c.a)
print(c._a)
