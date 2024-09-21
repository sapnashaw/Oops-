#8. Create an abstract base class `Shape` with an abstract method `area()`. Then create two subclasses
#   `Circle` and `Rectangle` that implement the `area()` method.

"""
To create an abstract base class Shape with an abstract method area() and then define two subclasses, Circle and Rectangle, that implement the area() method, you can use Python's abc module which provides infrastructure for defining abstract base classes.

Here’s how you can do it:

Define the abstract base class Shape:

Use the ABC class from the abc module.
Decorate the area method with @abstractmethod to declare it as an abstract method.
Implement the Circle and Rectangle subclasses:

Each subclass should provide its own implementation of the area() method.
"""
#Example :
  from abc import ABC,abstractmethod
  import math

# Define the abstract base class
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        """Method to calculate area, to be implemented by subclasses."""
        pass

# Define the Circle subclass
class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

# Define the Rectangle subclass
class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Example usage
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Circle area: {circle.area()}")        # Output: Circle area: 78.53981633974483
print(f"Rectangle area: {rectangle.area()}")  # Output: Rectangle area: 24

"""
  Explanation:
Abstract Base Class (Shape):

Inherits from ABC and defines the abstract method area(). This method does not have an implementation and must be overridden in any subclass.
Circle Class:

Implements the area() method to calculate the area of a circle using the formula 
𝜋
×
radius
2
π×radius 
2
 .
Rectangle Class:

Implements the area() method to calculate the area of a rectangle using the formula 
width
×
height
width×height.
Each subclass provides its specific implementation of the area() method, allowing for polymorphic behavior where different shapes compute their area in their own way.

"""