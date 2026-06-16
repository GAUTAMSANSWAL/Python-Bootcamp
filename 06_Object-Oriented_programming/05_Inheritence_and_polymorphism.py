# Inheritance is like a family tree. A child class (or subclass) inherits traits (attributes and methods) from its parent class (or superclass). This allows you to create new classes that are specialized versions of existing classes, without rewriting all the code.

class Animal: # Parent class (superclass)
    location = "Earth"  # Class attribute shared by all animals
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Some sound"
    
class Dog(Animal): # Child class (subclass) that inherits from Animal
    def speak(self):
        super().speak()  # Calls the speak method from the parent class (Animal)
        return "Woof!"
    
a = Animal("Generic Animal")
d = Dog("Buddy")

a.speak()  # Output: Some sound
d.speak()  # Output: Woof! 
print(d.location)  # Output: Earth (inherited from Animal)


# super(): Inside a child class, super() lets you call methods from the parent class. This is useful when you want to extend the parent's behavior instead of completely replacing it. It's especially important when initializing the parent class's part of a child object.