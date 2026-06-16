# 1. Create a Simple Class and Object
# Create a class Car with a method drive() that prints "Car is moving".
# Create an object of Car and call drive().

class Car:
    def __init__(self):
        pass

    def drive(self):
        print("Car is moving")

my_car = Car()
my_car.drive()  # Output: Car is moving


# 2. Constructor and Attributes
# Create a class Person with a constructor (__init__) that accepts name and age as arguments and stores them as instance attributes.
# Create an object and print the person’s name and age.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("Alice", 30)
person1.display_info()  # Output: Name: Alice, Age: 30


# 3. Simple Inheritance
# Create a base class Animal with a method sound() that prints "Some sound".
# Create a derived class Dog that overrides sound() to print "Bark!".
# Create an object of Dog and call sound().

class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark!")

my_dog = Dog()
my_dog.sound()  # Output: Bark!