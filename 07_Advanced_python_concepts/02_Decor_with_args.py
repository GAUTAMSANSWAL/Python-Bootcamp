# Decorators themselves can also accept arguments. This requires another level of nesting: an outer function that takes the decorator's arguments and returns the actual decorator function.

def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(num_times=3)
def hello_name(a):
    print(f"Hello {a}")

hello_name("Alice")  # This will print "Hello Alice" three times