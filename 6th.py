#6. Describe the five types of inheritance in Python.
#   Provide a simple example of multiple inheritance
"""
Inheritance in Python allows classes to inherit attributes and methods from other classes. Here are five common types of inheritance:

1. Single Inheritance
Definition: A class inherits from one parent class.

"""
class Parent:
    def parent_method(self):
        return "This is a parent method."

class Child(Parent):
    def child_method(self):
        return "This is a child method."

# Example usage
child = Child()
print(child.parent_method())  # Output: This is a parent method.
print(child.child_method())   # Output: This is a child method.

#2. Multiple Inheritance
# Definition: A class inherits from more than one parent class

class Mother:
    def mother_method(self):
        return "This is a mother method."

class Father:
    def father_method(self):
        return "This is a father method."

class Child(Mother, Father):
    def child_method(self):
        return "This is a child method."

# Example usage
child = Child()
print(child.mother_method())  # Output: This is a mother method.
print(child.father_method())  # Output: This is a father method.
print(child.child_method())   # Output: This is a child method.

#3. Multilevel Inheritance
#Definition: A class inherits from a parent class,and another class inherits from this child class.

class Grandparent:
    def grandparent_method(self):
        return "This is a grandparent method."

class Parent(Grandparent):
    def parent_method(self):
        return "This is a parent method."

class Child(Parent):
    def child_method(self):
        return "This is a child method."

# Example usage
child = Child()
print(child.grandparent_method())  # Output: This is a grandparent method.
print(child.parent_method())       # Output: This is a parent method.
print(child.child_method())        # Output: This is a child method.

#4. Hierarchical Inheritance
#Definition: Multiple classes inherit from a single parent class.

class Parent:
    def parent_method(self):
        return "This is a parent method."

class Child1(Parent):
    def child1_method(self):
        return "This is child1 method."

class Child2(Parent):
    def child2_method(self):
        return "This is child2 method."

# Example usage
child1 = Child1()
child2 = Child2()
print(child1.parent_method())  # Output: This is a parent method.
print(child2.parent_method())  # Output: This is a parent method.
print(child1.child1_method())  # Output: This is child1 method.
print(child2.child2_method())  # Output: This is child2 method.

#5. Hybrid Inheritance
#Definition: A combination of two or more types of inheritance.
#             It can involve multiple and hierarchical inheritance. 

class A:
    def method_a(self):
        return "Method from class A."

class B(A):
    def method_b(self):
        return "Method from class B."

class C(A):
    def method_c(self):
        return "Method from class C."

class D(B, C):
    def method_d(self):
        return "Method from class D."

# Example usage
d = D()
print(d.method_a())  # Output: Method from class A.
print(d.method_b())  # Output: Method from class B.
print(d.method_c())  # Output: Method from class C.
print(d.method_d())  # Output: Method from class D.
"""
Summary
Single Inheritance: One class inherits from another.
Multiple Inheritance: A class inherits from multiple parent classes.
Multilevel Inheritance: Inheritance forms a chain where each class inherits from the previous one.
Hierarchical Inheritance: Multiple classes inherit from a single parent class.
Hybrid Inheritance: A combination of multiple inheritance and hierarchical inheritance.
Each type of inheritance allows for different relationships and hierarchies among classes, providing flexibility in designing object-oriented systems.

"""