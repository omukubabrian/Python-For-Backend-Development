import math

class Shape:
    def area(self)->float:
        return 0

class Rectangle(Shape):
    def __init__(self,width:float,height:float)->None:
        self.width=width
        self.height=height

    def area(self)->float:
        return self.width *self.height

class Circle(Shape):
    def __init__(self,radius:float)->None:
        self.radius =radius

    def area(self) ->float:
        return math.pi * self.radius **2

s=Shape()
r=Rectangle(4,5)
c=Circle(3)

print(s.area())
print(r.area())
print(c.area())