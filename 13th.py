#13. Explain the concept of the Diamond Problem in multiple inheritance. How does Python resolve it?

"""
The Diamond Problem occurs in multiple inheritance when a class inherits from two classes that both inherit from a common ancestor,
creating ambiguity about which path to follow for method resolution.

Example structure:

      A
     / \
    B   C
     \ /
      D

Python's Resolution:
Python uses the C3 Linearization algorithm to determine the Method Resolution Order (MRO). This ensures a consistent order in which classes are searched for methods.
"""
#Example :
class A:
    def greet(self):
        return "Hello from A"

class B(A):
    def greet(self):
        return "Hello from B"

class C(A):
    def greet(self):
        return "Hello from C"

class D(B, C):
    pass

d = D()
print(d.greet())  # Output: "Hello from B"

#MRO Check:
#You can check the MRO with D.mro(), which shows the order Python will use to resolve methods, thus eliminating ambiguity.




