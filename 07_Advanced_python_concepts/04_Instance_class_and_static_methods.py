# In Python, methods within a class can be of three main types:

# 1. Instance Methods: These are the most common type of methods. They take self as the first parameter, which refers to the instance of the class. They can access and modify the instance's attributes.
# 2. Class Methods: These methods take cls as the first parameter, which refers to the class itself rather than an instance. They are defined using the @classmethod decorator and can access and modify class-level attributes.
# 3. Static Methods: These methods do not take self or cls as the first parameter. They are defined using the @staticmethod decorator and cannot access or modify instance or class-level attributes. They are typically used for utility functions that perform a task in isolation.

class Employee:

    company = "HP"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # by default this is an instance method
    def print_info(self):
        print(f"my name is {self.name} and my salary is {self.salary}")

    # Static method
    @staticmethod
    def total_salary_paid(s1,s2):
        print(f"total salary paid is {s1.salary + s2.salary}")

    # Class method
    @classmethod
    def print_company(cls):
        print(f"the company name is {cls.company}")
        
    # Class method to change the company name
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)

e1.print_info()  # my name is Alice and my salary is 50000
e2.print_info()  # my name is Bob and my salary is 60000

Employee.total_salary_paid(e1, e2)  # total salary paid is 110000

Employee.print_company()  # the company name is HP
Employee.change_company("Google")
Employee.print_company()  # the company name is Google