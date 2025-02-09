from abc import ABC, abstractmethod

# Import i użycie abc zabezpieczy przed utworzeniem obiektu bez implementcji określonej logiki

# Klasa abstrakcyjna Shape
class Shape(ABC):
    @abstractmethod
    def get_type(self):
        pass

# Podklasy
class Rectangle(Shape):
    def get_type(self):
        return "Type: rectangle"

class Triangle(Shape):
    def get_type(self):
        return "Type: triangle"

class Circle(Shape):
    def get_type(self):
        return "Type: circle"


class Factory:
    @staticmethod
    def create_shape(shape_type):
        shapes = {
            "rectangle": Rectangle,
            "triangle": Triangle,
            "circle": Circle
        }
        shape_class = shapes.get(shape_type.lower())

        if shape_class:
            return shape_class()
        else:
            print(f"Error: '{shape_type}' is not a valid shape type.")
            return None
