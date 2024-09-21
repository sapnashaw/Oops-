#7. What is the Method Resolution Order (MRO) in Python? How can you retrieve it programmatically?

"""
Method Resolution Order (MRO) in Python
Definition: The Method Resolution Order (MRO) is the order in which Python looks up methods and attributes in a class hierarchy. This is particularly important in cases of multiple inheritance, where a class inherits from more than one parent class. The MRO determines which method is invoked when multiple classes define a method with the same name.

Python uses the C3 linearization algorithm (also known as C3 superclass linearization) to determine the MRO. This algorithm ensures a consistent order in which base classes are searched, and it maintains the method resolution order based on the inheritance hierarchy.

Key Points:

The MRO ensures that each class in the hierarchy is visited in a specific order.
It maintains a consistent and predictable method resolution, even with complex inheritance structures.
Retrieving the MRO Programmatically
You can retrieve the MRO of a class using the __mro__ attribute or the mro() method. Here’s how you can do both
"""
#Using __mro__ Attribute:
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

# Retrieve MRO
print(D.__mro__)

#Output:
#(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

# Retrieve MRO
print(D.mro())

#Output:

#[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
"""
Explanation:
__mro__ Attribute: Returns a tuple of classes in the MRO, including the class itself and its base classes in the order they are searched.
mro() Method: Returns a list of classes in the MRO, including the class itself and its base classes in the order they are searched.
Both methods give you the MRO of the class D in this example. The order shows how Python will resolve method calls and attribute lookups when the class D is used.

"""