class Employee:
    company = "Google"  # Class attribute

    def __init__(self, name, salary, bond, company):
        self.name = name  # Instance attribute
        self.salary = salary  # Instance attribute
        self.bond = bond  # Instance attribute
        self.company = company  # Instance attribute (overrides class attribute)
    
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Bond: {self.bond} years")

e1 = Employee("Alice", 50000, 3, "Microsoft")
print(e1.company)  # Output: Microsoft (instance attribute overrides class attribute)

# Object introspection
print(dir(e1))  # Output: List of attributes and methods of the object.