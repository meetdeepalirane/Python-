'''
By default, Python does not provide abstract classes

Python comes with a module that provides the base for defining Abstract Base classes(ABC) and
that module name is ABC. ABC works by decorating methods of the base class as abstract and then
registering concrete classes as implementations of the abstract base.
A method becomes abstract when decorated with the keyword @abstractmethod.
'''


from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def calculate_area(self):
        print("in abstract clss")
class Circle(shape):
    def calculate_area(self,r):
        area=3.14*r*r
        print("Area of circle is",area)
class Triangle(shape):
    def calculate_area(self,h,b):
        area=h*b
        print("Area of Triangle is",area)

c=Circle()
c.calculate_area(5)

t=Triangle()
t.calculate_area(6.7,4.5)



