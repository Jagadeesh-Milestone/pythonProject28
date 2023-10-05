#__init__
#it is a special method in python oops.
#it is considered as a constructor/base of a class.
#a class allows only one constructor.
class lenovo:
    def __init__(self,ram,rom):
        self.ram=ram
        self.rom=rom
    def features(self):
        self.os='windows11'
        self.battery='5000mah'
        print(self.os,self.battery)
        print(self.ram)
        print(self.rom)
obj=lenovo('128gb','8gb')
obj.features()

