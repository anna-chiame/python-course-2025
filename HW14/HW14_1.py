"""Task 1
Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!"""

def logger(func) :
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} called with {', '.join(map(str, args))}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(4, 5)
square_all(2, 3, 4)