'''
Magic methods, also called dunder (double underscore) methods, are special methods in Python that have double underscores at the beginning and end of their names (e.g., __init__, __str__, __add__). These methods allow you to define how your objects interact with built-in Python operators, functions, and language constructs. They provide a way to implement operator overloading and customize the behavior of your classes in a Pythonic way.

Magic (dunder) methods are a powerful feature of Python that allows you to:

a) Customize how your objects interact with built-in operators and functions.
b) Make your code more intuitive and readable by using familiar Python syntax.
c) Implement operator overloading, container-like behavior, and other advanced features.
d) Define string representation.
'''

class Employee:

    company = "HP"
    
    # object initialization method
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    # string representation method
    def __str__(self):
        return f"my name is {self.name} and my salary is {self.salary}"
    
    # representation method
    def __repr__(self):
        return f"Employee({self.name}, {self.salary})"
    
    # Length method
    def __len__(self):
        return len(self.name)

e = Employee("Alice", 50000)
print(e.name, e.salary) # Alice 50000
print(e)  # my name is Alice and my salary is 50000, str method is called when we print the object
print(repr(e))  # Employee(Alice, 50000)
print(len(e))  # 5


'''
Operator Overloading: Python allows us to define the behavior of operators for user-defined classes. This is done by implementing special methods (also known as magic or dunder methods) in the class. For example, we can overload the addition operator (+) for our Employee class.

__add__ (+)
__sub__ (-)
__mul__ (*)
__eq__ (==)
__ne__ (!=)
__lt__ (<)
__gt__ (>)
__le__ (<=)
__ge__ (>=)
__truediv__ (/)
__floordiv__ (//)
__mod__ (%)
__pow__ (**)
'''