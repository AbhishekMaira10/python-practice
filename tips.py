""" Python tips with
     PEP8 style of writing cleaner code.
"""
# datetime
from sympy import Symbol, diff
import datetime
import time

NOW = datetime.datetime.now()
print(f"{NOW:%y-%m-%d %H:%m}")

# ternary operators
condition = True
if condition:
    x = 1
else:
    x = 0
print(x)
# or
x = 1 if condition else 0
print(x)

# f-string
name = "Eric"
age = 74
print(f"Hello, {name}. You are {age}.")

# pylint: disable = too-few-public-methods

# str and repr


class Comedian:
    """a class of comedian
    Returns:
        [string] -- A full name of a comedian with age.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name.lower()} {self.last_name.lower()} is {self.age}."


new_comedian = Comedian("Eric", "Idle", "24")
print(f"{new_comedian}")

# underscore placeholders
num1 = 10_000_000_000
num2 = 100_000_000
total = num1 + num2
print(f"{total:,}")

# enumerate
names = ["Corey", "Abhi", "Magnus", "Messi", "Matthew"]
for i, name in enumerate(names, start=1):
    print(i, name)

# Zip
names = ["Peter Parker", "Clark Kent", "Wade wilson", "Bruce Wayne"]
heroes = ["Spiderman", "Superman", "Deadpool", "Batman"]
universes = ["Marvel", "DC", "Marvel", "DC"]

for name, hero, universe in zip(names, heroes, universes):
    print(f"{name} is actually {hero} from {universe}")

# unpacking
a, b, *c = (1, 2, 3, 4, 5)
items = (0, 1, 2, 3, 4, 5, 6)
*_, a, b = items
print(a)
print(a, b, c)

# mutable default args


def display_time(time=None):
    """diaplays time
    Keyword Arguments:
        time {string} -- currrent time (default: {None})
    """
    print(datetime.datetime.now())
    time = datetime.datetime.now()
    print(time)
    print(f"{time:%y-%m-%d %H:%m}")


display_time()
time.sleep(10)
display_time()
time.sleep(1)

# switch case using dictionaries


def dispatch_dict(operator, x, y):
    """An implementation of switch case 
    statements in python using dictionaries

    Arguments:
        operator {String} -- type of operator
        x {Int} -- first input
        y {Int} -- second input
    """
    return {
        "add": lambda: x + y,
        "sub": lambda: x - y,
        "mul": lambda: x * y,
        "div": lambda: x / y,
    }.get(operator, lambda: None)()


operator, x, y = "mul", 8, 16
print(dispatch_dict(operator, x, y))

# derivatives in python
x = Symbol("x")
derivative = diff(x ** 2, x)
value = 20  # YOUR VALUE HERE
d = derivative.subs({x: value})
print(d)

# closures
"""
closures are inner functions that remembers and has access to the variables in the 
local scope in which it was created even after the outer function has finished executing 
"""


def outer_func(msg):
    message = msg

    def inner_func():
        # * message here is a free variable as it was not declared
        # *local to this function but is still being accessed
        print(message)

    return inner_func


hi_func = outer_func("hi")
hello_func = outer_func("hello")

print(hi_func)


# reversing a sequence

a = (1, 2, 3, 4, 5)
print(a[::-1])

# walrus operator- works only in python 3.8+

# a = ['j', 'a', 'k', 'd', 'c']
# if((n := len*(a))%2 == 1):
#    print(f"The number of letters is {n}, which is odd")

# using the joins() function

words = ("Hello", "python", "programmers")
print("!".join(words))

l = ["1", "2", "3", "5"]
print(",".join(l))

# most frequent element in the list
winnings = ["John", "Billy", "Sam", "Billy", "John", "John"]
print(max(set(winnings), key=winnings.count))

# track the frequencies of elements in a list

tracked = {item: winnings.count(item) for item in set(winnings)}
print(tracked)
print(sorted(tracked.items(), key=lambda x: x[1], reverse=True))

# using the any and all function
arrival_hours = {"Mon": 8.5, "Tue": 8.75, "wed": 9, "Thu": 8.5, "Fri": 8.5}
arrival_checks = [x > 8.75 for x in arrival_hours.values()]
print(any(arrival_checks))

arrival_checks_all = [x > 9.5 for x in arrival_hours.values()]
print(all(arrival_checks))

# custom reduce function


def my_reduce(function, iterable):
    it = iter(iterable)
    result = 0

    for x in it:
        result = function(result, x)
    return result


l = [1, 2, 3, 4, 5]
result = my_reduce(lambda x, y: x + y, l)

print(result)

# custom filter function


def filtered_vowel(alphabet):
    vowels = ["a", "e", "i", "o", "u"]
    return True if alphabet.lower() in vowels else False


def my_filter(function, iterable):
    it = iter(iterable)
    result = [x for x in it if function(x)]
    return result


alphabets = ["a", "b", "h", "i", "s", "h", "e", "k"]
result = my_filter(filtered_vowel, alphabets)

print(result)

#map with if statemennt can be done with filter function
arr_list = [-1, -2, -3, 1, 2, 3, 5]
result = list(map(lambda x: x**2, filter(lambda x: x > 0, arr_list)))
print(result)
