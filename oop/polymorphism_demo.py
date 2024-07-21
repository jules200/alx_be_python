import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        Shape.area = self.length * self.width
        return Shape.area
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        Shape.area = (self.radius ** 2) * math.pi
        return Shape.area