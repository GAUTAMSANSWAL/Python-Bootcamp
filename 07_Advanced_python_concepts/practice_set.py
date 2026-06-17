'''
1. Decorators in Python

a) Write a decorator logger that prints "Function is being called" before the function runs. Use it to decorate a function say_hello() that prints "Hello!".

b) Write a decorator timer that calculates how long a function takes to execute. Test it with a function that sums numbers from 1 to 1,000,000.
'''
# a) Decorator logger

def logger(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

@logger
def say_hello():
    print("Hello!")

say_hello()  # Output: Function is being called \n Hello!

# b) Decorator timer

import time

def timer(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print(f"Function took {end_time - start_time:.4f} seconds to execute")
        return result
    return wrapper

@timer
def sum_numbers():
    total = 0
    for i in range(1, 1000001):
        total += i
    return total

sum_numbers()  # Output: Function took X.XXXX seconds to execute

'''
2. Getters and Setters

a) Create a class Employee with a private attribute _salary.

Use @property to define a getter for salary.
Use @salary.setter to prevent setting negative values (print a warning instead).
Create an object and test by setting positive and negative salaries.
'''
class Employee:
    def __init__(self, _salary):
        self._salary = _salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, value):
        if value < 0:
            print("Warning: Salary cannot be negative.")
        else:
            self._salary = value

emp = Employee(50000)
print(emp.salary)  # Output: 50000
emp.salary = -60000
# Output: Warning: Salary cannot be negative.
print(emp.salary)  # Output: 50000 (unchanged)
emp.salary = 60000
print(emp.salary)  # Output: 60000 (updated)

'''
3. Static & Class Methods
a) Create a class MathUtils with:

A @staticmethod called add(a, b) that returns a + b.
A @classmethod called description(cls) that prints "This is a utility class for math operations."

b) Call both methods without creating an object.
'''
# a) class MathUtils
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    def description(cls):
        print("This is a utility class for math operations.")

# b) Call both methods without creating an object
print(MathUtils.add(5, 10))  # Output: 15
MathUtils.description(MathUtils)  # Output: This is a utility class for math operations.

'''
4. Magic/Dunder Methods
a) Create a class Book with attributes title and author.

Implement __str__() so that printing the object displays "Title by Author".
Implement __len__() so that len(book) returns the length of the title.

b) Create two Book objects and test these methods.
'''
# Creating class Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        print(f"{self.title} by {self.author}")
    def __len__(self):
        return len(self.title)
    
# Creating two Book objects for testing
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

# Testing __str__() method
book1.__str__()
book2.__str__()
# Testing __len__() method
print(len(book1))  # Output: 4 (length of title "1984")
print(len(book2))  # Output: 21 (length of title "To Kill a Mockingbird")

'''
5. Exception Handling and Custom Errors
a) Write a program that asks the user to enter a number and handles:

ValueError if the input is not a number
ZeroDivisionError if you try to divide by zero

b) Create a custom exception NegativeNumberError and raise it when the user enters a negative number.
'''
# a) Exception Handling
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result of division: {result}")
    # b) Custom Exception
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
except ValueError:
    print("ValueError: Please enter a valid number.")
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero.")

'''
6. map(), filter(), and reduce()
a) Use map() to convert [1, 2, 3, 4, 5] into their cubes.
b) Use filter() to get only even numbers from [10, 11, 12, 13, 14].
c) Use reduce() from functools to find the product of all elements in [1, 2, 3, 4].
'''
# a) Using map() to convert to cubes
numbers = [1, 2, 3, 4, 5]
cubes = list(map(lambda x: x**3, numbers))
print(cubes)  # Output: [1, 8, 27, 64, 125]

# b) Using filter() to get even numbers
numbers = [10, 11, 12, 13, 14]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [10, 12, 14]

# c) Using reduce() to find the product of all elements
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24 (1*2*3*4)

'''
7. Walrus Operator
a) Use the walrus operator to read input until the user enters "quit". Print each input as it is entered.
b) Use the walrus operator in a list comprehension to store lengths of words from ["python", "rocks", "ai"] in a list while filtering out words shorter than 4 characters.
'''

# a) Using walrus operator to read input until "quit"
while (user_input := input("Enter something (type 'quit' to exit): ")) != "quit":
    print(f"You entered: {user_input}")

# b) Using walrus operator in a list comprehension
words = ["python", "rocks", "ai"]
lengths = [length for word in words if (length := len(word)) >= 4]
print(lengths)  # Output: [6, 5] (lengths of "python" and "rocks")

'''
8. *args and **kwargs
a) Write a function sum_all(*args) that accepts any number of integers and returns their sum.
b) Write a function print_details(**kwargs) that prints key-value pairs passed as arguments, for example:
   print_details(name="Alice", age=25, city="Delhi")
   # Output:
   # name: Alice
   # age: 25
   # city: Delhi
'''
# a) Function sum_all(*args)
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total
sum_all(1, 2, 3, 4, 5)  # Output: 15

# b) Function print_details(**kwargs)
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_details(name="Alice", age=25, city="Delhi")