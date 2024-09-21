#5. What are the three types of access modifiers in Python? How are they denoted?

"""
In Python, access modifiers (or access specifiers) control the visibility and accessibility of class attributes and methods. Although Python does not enforce strict access control as some other programming languages do, it uses naming conventions to indicate the intended level of access. The three types of access modifiers in Python are:

1. Public
Definition: Public members (attributes or methods) are accessible from outside the class. They are not restricted and can be freely accessed and modified.

Notation: Public members do not have any special prefix.

"""
#example
class MyClass:
    def __init__(self, value):
        self.public_attribute = value
    
    def public_method(self):
        return "This is a public method."

# Example usage
obj = MyClass(10)
print(obj.public_attribute)  # Output: 10
print(obj.public_method())   # Output: This is a public method.

"""
2. Protected
Definition: Protected members are intended to be accessed only within the class itself and its subclasses (i.e., derived classes). 
They are not intended to be accessed from outside the class hierarchy.
"""
# Notation: Protected members are prefixed with a single underscore _.

class BaseClass:
    def __init__(self, value):
        self._protected_attribute = value
    
    def _protected_method(self):
        return "This is a protected method."

class DerivedClass(BaseClass):
    def __init__(self, value):
        super().__init__(value)

    def access_protected(self):
        return self._protected_method()

# Example usage
obj = DerivedClass(20)
print(obj.access_protected())  # Output: This is a protected method.
print(obj._protected_attribute)  # Output: 20 (not recommended but possible)

# In this example, _protected_attribute and _protected_method are meant to be accessed within the BaseClass and DerivedClass, 
# but they can still be accessed from outside the class if needed.

"""
2. Protected
Definition: Protected members are intended to be accessed only within the class itself and its subclasses (i.e., derived classes). They are not intended to be accessed from outside the class hierarchy.

Notation: Protected members are prefixed with a single underscore _.

"""
class BaseClass:
    def __init__(self, value):
        self._protected_attribute = value
    
    def _protected_method(self):
        return "This is a protected method."

class DerivedClass(BaseClass):
    def __init__(self, value):
        super().__init__(value)

    def access_protected(self):
        return self._protected_method()

# Example usage
obj = DerivedClass(20)
print(obj.access_protected())  # Output: This is a protected method.
print(obj._protected_attribute)  # Output: 20 (not recommended but possible)

#In this example, _protected_attribute and _protected_method are meant to be accessed within the BaseClass and DerivedClass, 
#but they can still be accessed from outside the class if needed.
"""
3. Private
Definition: Private members are intended to be accessible only within the class itself. They are not intended to be accessed from outside the class, including from subclasses.

Notation: Private members are prefixed with a double underscore __.

"""
class MyClass:
    def __init__(self, value):
        self.__private_attribute = value
    
    def __private_method(self):
        return "This is a private method."
    
    def access_private(self):
        return self.__private_method()

# Example usage
obj = MyClass(30)
print(obj.access_private())  # Output: This is a private method.

# Accessing private members directly from outside the class will raise an AttributeError
# print(obj.__private_attribute)  # Raises AttributeError
# print(obj.__private_method())   # Raises AttributeError

"""
In this example, __private_attribute and __private_method are private to MyClass and are not accessible directly from outside the class. However, Python’s name mangling mechanism renames private attributes in a way that they can be accessed using a different name, such as _MyClass__private_attribute, but this is not recommended.

Summary
Public: No special prefix, accessible from anywhere.
Protected: Single underscore prefix _, intended for internal use within the class and its subclasses.
Private: Double underscore prefix __, intended to be private to the class and not accessible from outside the class.
While Python relies on naming conventions for access control, it emphasizes the principle of "we are all consenting adults here," 
meaning developers should respect these conventions rather than enforcing strict access control.

"""