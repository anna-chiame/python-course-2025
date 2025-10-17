print("Task 3\n")

# this function makes a decorator with 3 rules:
def arg_rules(type_: type, max_length: int, contains: list):
    """ This function creates a decorator with 3 rules:
        1. Check if the argument has the right type.
        2. Check if the argument is not longer than max_length.
        3. Check if the argument contains all required symbols.
        """
    def decorator(func) :
        # the decorator
        def wrapper(*args, **kwargs):
            # get the first argument from the function for checking
            value = args[0]
            # check type
            if not isinstance(value, type_) :
                print(f"Error: argument must be {type_.__name__}")
                return False
            # check length
            if len(value) > max_length :
                print(f"Error: argument length must be <= {max_length}")
                return False
            # check if value has all symbols from the list
            for symbol in contains:
                if symbol not in value:
                    print(f"Error: argument must contain '{symbol}'")
                    return False
            # if all good go to the original function
            return func(*args, **kwargs)
        return wrapper
    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
help(arg_rules)
print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('S@SH05'))


