'''
*args and **kwargs are special syntaxes in Python function definitions that allow you to pass a variable number of arguments to a function. They are used when you don't know in advance how many arguments a function might need to accept.

*args: Allows you to pass a variable number of positional arguments.
**kwargs: Allows you to pass a variable number of keyword arguments.
'''

# *args (Positional Arguments)
# *args collects any extra positional arguments passed to a function into a tuple. The name args is just a convention; you could use any valid variable name preceded by a single asterisk (e.g., *values, *numbers).

def sum(*args):
    total = 0
    print(f"args: {args}")  # This will print the tuple of arguments passed
    for num in args:
        total += num
    return total

print(sum(1, 2, 3))  # Output: 6
print(sum(4, 5))     # Output: 9


# **kwargs (Keyword Arguments)
# **kwargs collects any extra keyword arguments passed to a function into a dictionary. Again, kwargs is the conventional name, but you could use any valid variable name preceded by two asterisks (e.g., **data, **options).

marks = {"Alice": 85, "Bob": 90, "Charlie": 78}
def print_marks(**kwargs):
    for item in kwargs.keys():
        print(f"the marks of {item} is {kwargs[item]}")
print_marks(**marks)


# Combining *args and **kwargs
# You can use both *args and **kwargs in the same function definition. The order is important: *args must come before **kwargs. You can also include regular positional and keyword parameters.

def func1(*args, **kwargs):
    print(f"args: {args}")  # This will print the tuple of positional arguments
    print(f"kwargs: {kwargs}")  # This will print the dictionary of keyword arguments

func1(1, 2, 3, name="Alice", age=30)