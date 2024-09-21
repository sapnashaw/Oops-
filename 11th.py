#11. Write a class that overrides the `__str__` and `__add__` magic methods. What will these methods allow
#    you to do?

"""
In Python, special or "magic" methods (methods with double underscores before and after their names) are used to define or override the behavior of built-in operations. The __str__ and __add__ methods are two such magic methods.

"""
#Here's how you can implement a class that overrides both __str__ and __add__:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Return a string representation of the Point object."""
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        """Return a new Point object which is the sum of this Point and another Point."""
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

# Example usage
p1 = Point(2, 3)
p2 = Point(4, 5)

# Using __str__ method
print(p1)  # Output: Point(2, 3)
print(p2)  # Output: Point(4, 5)

# Using __add__ method
p3 = p1 + p2
print(p3)  # Output: Point(6, 8)

"""
Explanation
__str__ Method:

Purpose: This method is used to define the string representation of an object. When you use the print() function or str() on an instance of the class, Python will call this method to obtain the string that represents the object.
Usage: In the example, print(p1) and print(p2) will produce human-readable output such as Point(2, 3) and Point(4, 5).
__add__ Method:

Purpose: This method defines the behavior of the + operator for instances of the class. It allows you to add two objects together using the + operator. The method should return the result of the addition.
Usage: In the example, p1 + p2 results in a new Point object where each coordinate is the sum of the corresponding coordinates of p1 and p2.
Benefits of Overriding These Methods
Custom String Representation: Overriding __str__ allows you to define how objects are represented as strings, which can be useful for debugging and logging.
Custom Addition Behavior: Overriding __add__ allows you to define how objects interact with each other using the + operator, making it possible to implement custom behaviors for mathematical operations or other forms of aggregation.
By implementing these methods, you can make your custom objects work more naturally with Python’s built-in operations and functions, enhancing their usability and integration with Python’s features.

"""