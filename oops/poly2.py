#polymorphism in oops:
class bird:
    def fly(self):
        print('some birds can fly some birds cannot fly')
class eagle(bird):
    def fly(self):
        print('eagle can fly at very heights')
class parrot(bird):
    def fly(self):
        print('parrot can fly but not at very heights')
class ostrich(bird):
    def fly(self):
        print('ostrich cannot fly')
o=ostrich()
o.fly()

p=parrot()
p.fly()

e=eagle()
e.fly()