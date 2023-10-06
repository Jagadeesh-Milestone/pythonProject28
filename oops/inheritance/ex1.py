#inheritance:
#inheritance is the property in which one class is getting the all
#attributes and methods of another class.
#python has five types of inheritance.
#single inheritance
#multi level inheritance
#multiple inheritance
#hirerarchal inheritance
#hybrid inheritance

#here the class which is inherited is called child/sub/derived class
#and the class from where the class being inherited is called parent/
#super/base class.

#single inheritance:
#it is the property in which a single class is derived from a
#single parent class.
class parent:
    def d1(self):
        print('I am parent property')
class child(parent):
    def d2(self):
        print('I am a child property')
c=child()
c.d1()
c.d2()

