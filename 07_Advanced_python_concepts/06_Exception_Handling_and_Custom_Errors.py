# Exceptions are events that occur during the execution of a program that disrupt the normal flow of instructions. Python provides a robust mechanism for handling exceptions using try-except blocks. This allows your program to gracefully recover from errors or unexpected situations, preventing crashes and providing informative error messages. You can also define your own custom exceptions to represent specific error conditions in your application.
'''
Basic Exception Handling
The try-except block is the fundamental construct for handling exceptions:

The try block contains the code that might raise an exception.
The except block contains the code that will be executed if a specific exception occurs within the try block.
'''

try:
    x = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
# gets executed when there is no error
else:
    print("everything went well")
finally:
    print("This block will always execute, regardless of whether an exception occurred or not.")


# Raising Exceptions (raise)
# You can manually raise exceptions using the raise keyword. This is useful for signaling error conditions in your own code.

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        raise ValueError("You must be at least 18 years old.")
    else:
        print("Age is valid.")

try:
    check_age(-5)
except ValueError as e:
    print(f"Error: {e}")
try:
    check_age(15)
except ValueError as e:
    print(f"Error: {e}")    
try:
    check_age(25)
except ValueError as e:
    print(f"Error: {e}")