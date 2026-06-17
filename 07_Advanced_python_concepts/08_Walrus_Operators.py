# The walrus operator (:=), introduced in Python 3.8, is an assignment expression operator. It allows you to assign a value to a variable within an expression. This can make your code more concise and, in some cases, more efficient by avoiding repeated calculations or function calls. The name "walrus operator" comes from the operator's resemblance to the eyes and tusks of a walrus.

def very_slow_function():
    print("Starting a very slow function...")
    print("Starting a very slow function...")
    print("Starting a very slow function...")
    print("Starting a very slow function...")
    print("Starting a very slow function...")
    print("Starting a very slow function...")
    return 42

a = very_slow_function()  # This will call the function and assign the result to 'a'
if a > 100:
    print("a is greater than 100")
else:
    print("a is not greater than 100")


# alternate optional way to use the walrus operator
if((a:= very_slow_function())>100):
    print("a is greater than 100")
else:
    print("a is not greater than 100")