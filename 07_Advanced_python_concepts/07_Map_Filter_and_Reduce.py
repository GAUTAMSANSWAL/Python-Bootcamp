# map, filter, and reduce are higher-order functions in Python (and many other programming languages) that operate on iterables (lists, tuples, etc.). They provide a concise and functional way to perform common operations on sequences of data without using explicit loops. While they were more central to Python's functional programming style in earlier versions, list comprehensions and generator expressions often provide a more readable alternative in modern Python.
'''
Map
The map() function applies a given function to each item of an iterable and returns an iterator that yields the results.

Syntax: map(function, iterable, ...)

function: The function to apply to each item.
iterable: The iterable (e.g., list, tuple) whose items will be processed.
...: map can take multiple iterables. The function must take the same number of arguments
'''
# Example of map

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]

a = list(map(square, numbers))
print(a)

# alternate using lambda

b = list(map(lambda x: x * x, numbers))
print(b)

# alternate using list comprehension

c = [x * x for x in numbers]
print(c)

# Example of map with multiple iterables

n1 = [1, 2, 3]
n2 = [4, 5, 6]

summed = list(map(lambda x,y: x+y, n1, n2))
print(summed)  # [5, 7, 9]


'''
Filter
The filter() function constructs an iterator from elements of an iterable for which a function returns True. In other words, it filters the iterable based on a condition.

Syntax: filter(function, iterable)

function: A function that returns True or False for each item. If None is passed, it defaults to checking if the element is True (truthy value).
iterable: The iterable to be filtered.
'''
# Example of filter

def greater_than_9(n):
    if n>9:
        return True
    else:
        return False
    
numbers1 = [1,765,5366,9,657,45,683,3,7,976,2,45,4,3,2]
greater_than_9_list = list(filter(greater_than_9, numbers1))
print(greater_than_9_list) 

# alternate using lambda

greater_than_9_list_d = list(filter(lambda x : x>9 , numbers1))
print(greater_than_9_list_d) 

# alternate using list compreehnsion

greater_than_9_list_c = [x for x in numbers1 if x>9]
print(greater_than_9_list_c)


'''
Reduce
The reduce() function applies a function of two arguments cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single value. reduce is not a built-in function; it must be imported from the functools module.

Syntax: reduce(function, iterable[, initializer])

function: A function that takes two arguments.
iterable: The iterable to be reduced.
initializer (optional): If provided, it's placed before the items of the iterable in the calculation and serves as a default when the iterable is empty.
'''
from functools import reduce

# Example of reduce

def add(x, y):
    return x + y
numbers2 = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(add, numbers2)
print(sum_of_numbers)  # 15

def multiply(x, y):
    return x * y
product_of_numbers = reduce(multiply, numbers2)
print(product_of_numbers)  # 120

# alternate using lambda

sum_of_numbers_lambda = reduce(lambda x, y: x + y, numbers2)
print(sum_of_numbers_lambda)  # 15

product_of_numbers_lambda = reduce(lambda x, y: x*y, numbers2)
print(product_of_numbers_lambda)  # 120