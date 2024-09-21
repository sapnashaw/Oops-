#3. Explain the difference between instance methods and class methods. Provide an example of each

"""
Instance Methods
Definition: Instance methods are the most common type of methods in Python classes. They operate on an instance of the class (i.e., they work with the object created from the class). Instance methods can access and modify the object's attributes and call other instance methods.

Syntax: Instance methods take self as their first parameter, which represents the instance of the class.

    """
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} is barking."

# Example usage
dog = Dog("Rex", 5)
print(dog.bark())  # Output: Rex is barking.
    
""" 
  Class Methods
Definition: Class methods operate on the class itself rather than on instances of the class. They can be used to access or modify class state that applies across all instances. Class methods are often used for factory methods or alternative constructors.

Syntax: Class methods take cls as their first parameter, which represents the class itself.

Decorator: You use the @classmethod decorator to define a class method.   

""" 
class Dog:
    species = "Canis lupus familiaris"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def get_species(cls):
        return cls.species

# Example usage
print(Dog.get_species())  # Output: Canis lupus familiaris


   