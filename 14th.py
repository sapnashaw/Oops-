#14. Write a class method that keeps track of the number of instances created from a class.

  #You can create a class method in Python to keep track of the number of instances created from a class by maintaining a class variable that increments every time a new instance is initialized.
  # Here’s how you can implement this:
  
class InstanceCounter:
    instance_count = 0  # Class variable to track the number of instances

    def __init__(self):
        InstanceCounter.instance_count += 1  # Increment the count on initialization

    @classmethod
    def get_instance_count(cls):
        return cls.instance_count  # Return the current instance count

# Example usage
obj1 = InstanceCounter()
obj2 = InstanceCounter()
obj3 = InstanceCounter()

print(InstanceCounter.get_instance_count())  # Output: 3

#Explanation:
#instance_count: A class variable that keeps track of the number of instances.
#_init__ method: Each time an instance is created, this method increments instance_count.
#get_instance_count: A class method that returns the total number of instances created.
#You can create instances of InstanceCounter, and call get_instance_count() to see how many have been created.
