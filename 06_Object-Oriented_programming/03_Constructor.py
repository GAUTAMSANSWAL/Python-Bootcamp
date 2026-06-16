# The __init__ method is special. It's called the constructor. It's automatically run whenever you create a new object from a class.

# What's it for? The constructor's job is to initialize the object's attributes – to give them their starting values. It sets up the initial state of the object.

class Employee:
    def __init__(self, name, salary, bond):
        self.name = name
        self.salary = salary
        self.bond = bond

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Bond: {self.bond} years")


e1 = Employee("John", 34000, 2)
e1.get_info()  # Output: Name: John, Salary: 34000, Bond: 2 years