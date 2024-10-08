from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        "Must be implemented in subclass"
        pass

    @abstractmethod
    def perimeter(self):
        "Must be implemented in subclass"
        pass


class Rectangle(Shape):
    def __init(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        raise NotImplemented("Not implemented")


class Circle(Shape):

    def __init(self, radius):
        self.radius = radius

    def area(self):
        return (self.radius ** 2) * math.pi

    def perimeter(self):
        return 2 * math.pi * self.radius


circle = Circle(4)
rectangle = Rectangle(2, 2)
circle.area()
rectangle.area()
