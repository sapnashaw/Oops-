# 4. How does Python implement method overloading? Give an example.

"""
In Python, method overloading, as seen in some other languages like Java, is not natively supported in the same way. In those languages, method overloading allows multiple methods with the same name but different parameters. Python does not directly support this because it uses a single method definition to handle different types or numbers of arguments.

Instead, Python achieves similar functionality through default arguments, variable-length argument lists, and by manually handling different argument types within a single method. Here’s how you can implement method overloading-like behavior in Python:

Using Default Arguments
You can use default arguments to create methods that can handle different numbers of arguments.

"""
class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c

# Example usage
math = MathOperations()
print(math.add(5, 3))    # Output: 8 (using two arguments)
print(math.add(5, 3, 2)) # Output: 10 (using three arguments)

"""
Using Variable-Length Arguments
Python allows you to handle variable numbers of arguments using *args and **kwargs.
"""

class MathOperations:
    def add(self, *args):
        return sum(args)

# Example usage
math = MathOperations()
print(math.add(5, 3))          # Output: 8 (using two arguments)
print(math.add(5, 3, 2))       # Output: 10 (using three arguments)
print(math.add(1, 2, 3, 4, 5)) # Output: 15 (using five arguments)

# Manually Handling Different Types
# You can also manually handle different types of arguments within a single method.
class Greeter:
    def greet(self, *args):
        if len(args) == 1:
            if isinstance(args[0], str):
                return f"Hello, {args[0]}!"
            elif isinstance(args[0], list):
                return "Hello, " + ", ".join(args[0]) + "!"
        elif len(args) == 2:
            return f"Hello, {args[0]} and {args[1]}!"
        else:
            return "Hello, everyone!"

# Example usage
greeter = Greeter()
print(greeter.greet("Alice"))            # Output: Hello, Alice!
print(greeter.greet(["Alice", "Bob"]))   # Output: Hello, Alice, Bob!
print(greeter.greet("Alice", "Bob"))     # Output: Hello, Alice and Bob!
print(greeter.greet())                   # Output: Hello, everyone!

"""
Summary
While Python does not support method overloading directly like some other languages, you can achieve similar functionality through:

Default arguments: Providing default values for some parameters.
Variable-length arguments: Using *args for an arbitrary number of positional arguments.
Manual argument handling: Implementing logic within a single method to handle different argument types and counts.

"""