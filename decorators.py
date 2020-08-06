# decorators
"""
decorators are function that take in another function as an argument,
adds some functionality to it and return another function without
 changing the original source code of the function you passed in
"""

import time
from functools import wraps

def decorator_function(original_function):

    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)
    return wrapper_function


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(
            f'call method executed this before {self.original_function.__name__}')
        return self.original_function(*args, **kwargs)


@decorator_function
def dispaly():
    print("display function ran")


@decorator_class
def display_info(name, age):
    print(f'display_info ran with arguments {name} and {age}')


dispaly()

display_info('abhishek', 20)

# practical examples


def my_logger(original_function):
    import logging
    logging.basicConfig(
        filename=f'{original_function.__name__}.log', level=logging.INFO)

    @wraps(original_function)
    def wapper_function(*args, **kwargs):
        logging.info(f'Ran with args: {args}, and kwargs: {kwargs}')
        return original_function(*args, **kwargs)

    return wapper_function


def my_timer(original_function):
    import time

    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{original_function.__name__} ran {t2} seconds')
        return result

    return wrapper_function

@my_logger
@my_timer
def displayinfo(name, age):
    time.sleep(1)
    print(f'displayinfo ran with arguments {name} and {age}')


displayinfo('abhishek maira', 20)
