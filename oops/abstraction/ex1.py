#abstraction:
#it is the property in which hiding the unnecessary information and
#displaying the necessary information:
#to use abstraction we have to import it from ABC:
from abc import ABC,abstractmethod
class polygon(ABC):
    @abstractmethod
    def sides(self):
        print('polygon has many sides')
class triangle(polygon):
    def sides(self):
        print('triangle has three sides')
class square(polygon):
    def sides(self):
        print('square has four sides')
s=square()
s.sides()

t=triangle()
t.sides()

p=polygon()
p.sides()


