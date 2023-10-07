#polymorphism in vehicles:
class vehicle:
    def transport(self):
        print('vehicles are used to travel')
class car(vehicle):
    def transport(self):
        print('car is used to travel on roads')
class ship(vehicle):
    def transport(self):
        print('ship is used to travel on water')
class aeroplane(vehicle):
    def transport(self):
        print('aeroplane is used to travel on air')
a=aeroplane()
a.transport()

s=ship()
s.transport()

c=car()
c.transport()

