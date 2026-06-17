# Decorators take functions as arguments, make a new function inside its body (wrapper function) and return the wrapper function. The wrapper function can modify the behavior of the original function.

def decorator_function(original_function):
    def wrapper_function():
        print("it will now execute the original function")
        original_function()
        print("it has executed the original function")
    return wrapper_function

@decorator_function
def print_hello():
    print("Hello")

print_hello()  # it will now execute the original function

# decorator_function(print_hello)()  # it will now execute the original function