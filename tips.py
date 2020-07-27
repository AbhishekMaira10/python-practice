""" Python tips with
     PEP8 style of writing cleaner code.
"""
# datetime
import copy
import secrets
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

# map with if statemennt can be done with filter function
arr_list = [-1, -2, -3, 1, 2, 3, 5]
result = list(map(lambda x: x**2, filter(lambda x: x > 0, arr_list)))
print(result)

# to create a secret key(a big random set of characters)
#import secrets
secret_key = secrets.token_hex(16)
print(secret_key)

# finding min and max index
numbers = [32, 12, 4, 122, 123]

# simple way
index_min = numbers.index(min(numbers))
index_max = numbers.index(max(numbers))

# using lambdas
index_min2 = min(enumerate(numbers), key=lambda x: x[1])[0]
index_max2 = max(enumerate(numbers), key=lambda x: x[1])[0]


# difference between shallow copy and deep copy

# by creating a shallow copy adding a new object
# to the original collection, li3, doesn’t propagate to li4,
# but modifying one of the objects in li3 will propagate to li4.
li3 = [['a'], ['b'], ['c']]
li4 = list(li3)
li3.append([4])
print(li4)
print(li3)

li3[0][0] = ['X']
# print(li4)

# by creating a deep copy The 2 objects are now completely
# independent and changes to either have no affect on the other.
li5 = [['a'], ['b'], ['c']]
li6 = copy.deepcopy(li5)
li5.append([4])
li5[0][0] = ['X']
print(li6)

# binary of an integer
print(bin(5))

# removing whitespaces from a string
s = 'A string with     white space'
print(''.join(s.split()))

# diference between instance, static and class methods in python


class CoffeeShop:
    specialty = 'espresso'

    def __init__(self, coffee_price):
        self.coffee_price = coffee_price

    # instance method
    # accept self parameter and relate to a specific instance of the class.
    def make_coffee(self):
        print(f'Making {self.specialty} for ${self.coffee_price}')

    # static method
    # use @staticmethod decorator, are not related to a specific instance,
    # and are self-contained (don’t modify class or instance properties)
    @staticmethod
    def check_weather():
        print('Its sunny')

    # class method
    # accept cls parameter and can modify the class itself
    @classmethod
    def change_specialty(cls, specialty):
        cls.specialty = specialty
        print(f'Specialty changed to {specialty}')


coffee_shop = CoffeeShop('5')
coffee_shop.make_coffee()
coffee_shop.check_weather()
coffee_shop.change_specialty('drip coffee')


# Reversing a list in python

# Method 1: Using the reversed() built-in function.

# In this method, we neither reverse a list in-place(modify the original list),
# nor we create any copy of the list. Instead, we get a reverse iterator which we
# use to cycle through the list.

def Reverse(lst):
    return [ele for ele in reversed(lst)]


# Driver Code
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))

# Method 2: Using the reverse() built-in function.

# Using the reverse() method we can reverse the contents of the list object
# in-place i.e., we don’t need to create a new list instead we just copy the
# existing elements to the original list in reverse order. This method directly
# modifies the original list.


def Reverse2(lst):
    lst.reverse()
    return lst


lst = [10, 11, 12, 13, 14, 15]
print(Reverse2(lst))

# Method 3: Using the slicing technique.

# In this technique, a copy of the list is made and the list is not sorted
# in-place. Creating a copy requires more space to hold all of the existing
# elements. This exhausts more memory.filter_none


def Reverse3(lst):
    new_lst = lst[::-1]
    return new_lst


lst = [10, 11, 12, 13, 14, 15]
print(Reverse3(lst))
