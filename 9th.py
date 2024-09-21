# 9. Demonstrate polymorphism by creating a function that can work with different shape objects to calculate
#    and print their areas.

"""
Polymorphism allows different classes to be treated as instances of the same class through a common interface. In this case, we can demonstrate polymorphism by creating a function that can work with different shape objects and calculate and print their areas.

Here’s how you can do it using the Shape, Circle, and Rectangle classes defined previously:

"""
from abc import ABC, abstractmethod
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

# Function that uses polymorphism
def print_area(shape):
    """Calculate and print the area of the given shape."""
    if not isinstance(shape, Shape):
        raise TypeError("Object must be an instance of Shape")
    print(f"Area: {shape.area()}")

# Example usage
circle = Circle(5)
rectangle = Rectangle(4, 6)

print_area(circle)      # Output: Area: 78.53981633974483
print_area(rectangle)  # Output: Area: 24

"""
Explanation
Abstract Base Class (Shape):

Defines the area() method that must be implemented by any subclass.
Subclasses (Circle and Rectangle):

Both classes implement the area() method, each with its own logic for calculating the area.
Polymorphic Function (print_area):

Takes a Shape object as a parameter.
Uses the area() method of the shape object to calculate and print the area.
The function does not need to know the specific type of shape; it relies on the common interface provided by the Shape class.
Benefits of Polymorphism
Flexibility: The print_area function can work with any shape that implements the Shape interface. This makes the code more flexible and reusable.
Maintainability: Adding new shapes only requires implementing the Shape interface without modifying the print_area function.
This demonstrates how polymorphism allows different classes to be used interchangeably through a common interface, facilitating code that is more modular and easier to maintain.

"""