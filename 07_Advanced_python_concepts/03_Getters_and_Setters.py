# Getters and Setters are methods that allow you to control access to the attributes of a class. They are used to encapsulate the internal representation of an object and provide a way to access and modify the attributes in a controlled manner.
# Using getters and setters can help you to validate the data before setting it, and to provide a way to access the attributes without directly exposing them.

# a) Encapsulate data and enforce validation: You can check if the new value meets certain criteria before assigning it.
# b) Control access to "private" attributes: By convention, attributes starting with an underscore are considered private, and external code should use getters/setters instead of direct access.
# c) Make the code more maintainable: Changes to the internal representation of an object don't necessarily require changes to code that uses the object.
# d) Add additional logic: Logic can be added when getting or setting attributes.

# Using getters and setters

# 1. Traditional Approach (Using Methods)
# A basic approach is to use explicit getter and setter methods:

class Person:
    def __init__(self, name):
        self._name = name  # Convention: underscore (_) denotes a private attribute.

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name 

p = Person("Alice")
print(p.get_name())  # Alice
p.set_name("Bob")
print(p.get_name())  # Bob 

# 2. Using @property (Pythonic Approach)
# Python provides a more elegant and concise way to implement getters and setters using the @property decorator. This allows you to access and modify attributes using the usual dot notation (e.g., p.name) while still having the benefits of getter and setter methods.

class People:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

p = People("Alice")
print(p.name)  # Alice
p.name = "Bob"
print(p.name)  # Bob


# Benefits of @property:

# Attribute-like access: You can use obj.name instead of obj.get_name() and obj.set_name(), making the code cleaner and more readable.
# Consistent interface: The external interface of your class remains consistent even if you later decide to add validation or other logic to the getter or setter.
# Read-only properties: You can create read-only properties by simply omitting the @property.setter method (see the next section).
# @property.deleter: deletes a property. Here is an example:

class Employee:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    @name.deleter
    def name(self):
        del self._name

e = Employee("Alice")
print(e.name)  # Alice
e.name = "Bob"
print(e.name)  # Bob
del e.name
# print(e.name)  # This will raise an AttributeError since the name attribute has been deleted.